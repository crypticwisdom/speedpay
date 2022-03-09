from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from product.serializers import ProductSerializer
from product.models import Product
# Create your views here.


class ProductView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):

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



