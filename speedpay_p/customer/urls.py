from django.urls import path
from .views import CustomerSignUp, LogoutView, CustomerLoginView

app_name = "customer"

urlpatterns = [
    path("signup/", CustomerSignUp.as_view(), name="sign_up"),
    path("login/", CustomerLoginView.as_view(), name="login"),


    path("logout/", LogoutView.as_view(), name="customer_logout"),
]