from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
#
from product.serializers import ProductSerializer
from .serializers import SuperUserSignUpSerializer, UserSerializer, AdminCreateProductSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from product.models import Product
# Create your views here.


class SuperUserSignUp(APIView):
    permission_classes = [AllowAny]

    # A get request to this View will response with this get method.
    def get(self, request):
        return Response({
            "Message": "Welcome to the SignUp page, Please Sign-Up with your credentials (username and password) ... "})

    #  A POST request will SignUp or Register as SuperUSer
    def post(self, request):
        try:
            data = request.data
            serializer = SuperUserSignUpSerializer(data=data)
            if serializer.is_valid():
                super_user = User.objects.create_superuser(
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    email=data.get('email'),
                    username=data.get('username'),
                    is_staff=True,
                    is_superuser=True,
                    is_active=True,
                    password=data.get('password')
                )
                da = {"first_name": super_user.first_name, "last_name": super_user.last_name,
                      "email": super_user.email, "username": super_user.username, "is_staff": super_user.is_staff,
                      "is_superuser": super_user.is_superuser}

                # Get user token, include refresh and access token
                return Response({
                    "success": True,
                    "message": "Thank You for signing up Admin",
                    'detail': da,
                    # It's not really neccessary to return tokens here,
                    # because not all user might login after signup.
                    # "access token": f"{str(AccessToken.for_user(super_user))}",
                    # "refresh token": f"{str(RefreshToken.for_user(super_user))}"
                })
            else:
                return Response({"message": serializer.errors, "status": status.HTTP_403_FORBIDDEN})
        except Exception as err:
            return Response({
                "message": str(err),
                "status": status.HTTP_403_FORBIDDEN
                })


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                print(request.user.last_name)
                return Response({"message": "Already Authenticated"})

            username = request.data.get('username')
            password = request.data.get('password')
            response = dict()

            # Check if username Exist
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                response['detail'] = "Username Provided is not Valid"
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    user_serializer = UserSerializer(user).data
                    response['detail'] = "You are logged In"
                    print(request.user)
                    return Response({'success': True,
                                     "user": user_serializer,
                                     "detail": response,
                                     "token": {"access": f"{AccessToken.for_user(user)}",
                                               "refresh": f"{RefreshToken.for_user(user)}"
                                               }
                                     })
                response['detail'] = "You Details were not found"
            return Response({'success': False, "detail": response, "status": status.HTTP_403_FORBIDDEN})
        except (KeyError, Exception) as err:
            return Response({"success": False, "detail": str(err), "status": status.HTTP_403_FORBIDDEN})


class DashBoard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "hello"})


#  List and Create Product
class AdminCrudProduct(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get(self, request):
        try:
            query = Product.objects.all()
            serializer = ProductSerializer(query, many=True).data
            if 'category' in request.GET:
                data = request.GET['category'].capitalize()
                print(request.GET)
                query = Product.objects.filter(categories__name=data)
                serializer = ProductSerializer(query, many=True).data

            return Response({"message": "EveryOne can view this products ...", "detail": serializer})
        except (Exception, KeyError) as err:
            return Response(str(err))

    def post(self, request):
        try:
            data = request.data
            #     takes in (name, title, categories, description, size, price, quantity)
            # serializer = ProductSerializer()

            # name = data.get('name')
            # title = data.get('title')
            # description = data.get('description')
            # categories = data.get('categories')
            # size = data.get('size')
            # price = data.get('price')
            # quantity = data.get('quantity_avaliable')

            serializer = AdminCreateProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print("done")
            else:
                return Response({"m": serializer.errors})
            return Response({"success": True,
                             "detail": serializer.data,
                             "message": f"Successfully Created Product {data.get('name', '')}",
                             "status": status.HTTP_200_OK})

        except (Exception, ) as err:
            return Response({"error": str(err)})

    def put(self, request, slug):
        if slug is None:
            return Response({"message": "Product Not Found.",
                             "status": status.HTTP_403_FORBIDDEN})
        try:
            data = request.data
            product = Product.objects.get(slug=slug)

            product.name = data.get("name", "")
            product.title = data.get("title", "")
            product.description = data.get("description", "")
            product.categories; print(product.categories)
            product.size = data.get("size", '')
            product.price = data.get("price", "")
            product.quantity_available = data.get("quantity", "")

            return Response({"success": True, "detail": "Product Detail", "status": status.HTTP_201_CREATED})
        except Exception as err:
            return Response({"detail": str(err),
                             "message": "Product Not Found.",
                             "status": status.HTTP_403_FORBIDDEN})


class LogoutView(APIView):
    # Only login SuperUser has View
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request=request)
        print(request.user)
        return Response({"success": True, "message": "You have successfully logout"})