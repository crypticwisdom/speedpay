from django.db import models
# from merchant.models import Merchant
from uuid import uuid4
from product.models import Product
# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=200, null=False, default="")
    # merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name="product")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

