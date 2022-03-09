from django.db import models
from uuid import uuid4
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, default="")
    title = models.CharField(max_length=200, null=True, default="product title")
    description = models.TextField(blank=True)
    # brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, default=str(uuid4())[:10])
    categories = models.ManyToManyField(Category, related_name='category')
    size = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    quantity_available = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f"{self.name}-{self.title}")
