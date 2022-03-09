from django.contrib import admin
from customer.models import Customer
# from merchant.models import Merchant
from store.models import Store
from product.models import Product, Category


# Register your models here.


admin.site.register(Customer)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(Customer)