from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
# Import Super User LogOut View
from superuser.views import LogoutView

# Create your views here.

"""This view will handle customer sign_up, login and logout also"""


class CustomerSignUp(APIView):

    def post(self, request, *args, **kwargs):
        # firstname, lastname, phone_number, email, address
        response = dict()
        try:
            data = request.data
            customer_user = User.objects.create_user(
                username=data.get("username", ''),
                first_name=data.get("firstname", ''),
                last_name=data.get("lastname", ''),
                email=data.get("email", ''),
                is_staff=False,
                is_superuser=False,
                is_active=True,
                password=data.get('password', '')

            )
            # Associate this user instance with a Customer Instance to Complete SignUp Process.
            print(customer_user)

            if customer_user is not None:
                telephone = data.get('phone_number', '')
                # print(telephone[-10:])
                customer = Customer.objects.create(
                    user=customer_user,
                    phone_number=f"+234{telephone[-10:]}",
                    email=data.get("email", "")
                )
                print(customer.email)

        except (KeyError, Exception) as err:
            return Response({"message": False, "response": f"{err}", "status": status.HTTP_403_FORBIDDEN})
        else:
            return Response({"success": True,
                             "response": f"{response}",
                             "status": status.HTTP_201_CREATED
                             })


class CustomerLoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        response = dict()
        try:
            if request.user.is_authenticated:
                print(request.user)
                return Response({"response": "This user is already Authenticated",
                                 "status": status.HTTP_403_FORBIDDEN})
            data = request.data
            username = data.get("username", "")
            password = data.get("password", "")

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist as er:
                return Response({"success": False, "error_message": str(er), "response": "Username is not Valid",
                                 "status": status.HTTP_403_FORBIDDEN})

            user_auth = authenticate(request, username=username, password=password)
            if user_auth is not None:
                print("loggin in")
                login(request, user_auth)
            else:
                print("login else error")
                return Response({"success": False, "response": "Failed to authenticate user details",
                                 "status": status.HTTP_403_FORBIDDEN})
            print("Inner")
        except (KeyError, Exception) as err:
            return Response({"success": False, "error_message": str(err), "response": "Username is not Valid",
                             "status": status.HTTP_403_FORBIDDEN})
        else:
            #  If authentication was done successfully
            print(request.user)
            return Response({"success": True, "response": "Login was Successful",
                             "status": status.HTTP_200_OK,
                             "details": "",
                             "tokens": {
                                 "refresh_token": str(f"{RefreshToken.for_user(request.user)}"),
                                 "access_token": str(f"{AccessToken.for_user(request.user)}")
                             }})
