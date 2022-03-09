from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from product.models import Product

class SuperUserSignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff', 'is_superuser',
                  'is_active', 'username', 'password']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


class AdminCreateProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'title', 'description',
                  'categories', 'size', 'price', 'quantity_available']





