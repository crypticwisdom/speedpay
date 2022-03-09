from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, null=False, default=str(uuid4())[:10])
    image = models.ImageField(upload_to="customer-images/", null=True, blank=True)
    file = models.FileField(upload_to="customer-files", null=True, blank=True)
    phone_number = models.CharField(max_length=17, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return str(f"{self.user}-{self.email}-{self.phone_number}")



