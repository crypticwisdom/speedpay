from django.urls import path
from product.views import ProductView


app_name = "product"

urlpatterns = [
    path("product-list", ProductView.as_view(), name="product_list"),

]