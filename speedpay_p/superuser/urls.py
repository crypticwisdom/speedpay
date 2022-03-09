from django.urls import path
from .views import SuperUserSignUp, LoginView, DashBoard, LogoutView, AdminCrudProduct
app_name = 'superuser'

urlpatterns = [
    path('', SuperUserSignUp.as_view(), name="sign_up"),
    path('login', LoginView.as_view(), name="login"),
    path('dashboard', DashBoard.as_view(), name="dashboard"),
    path('product', AdminCrudProduct.as_view(), name="product"),
    path('add-product', AdminCrudProduct.as_view(), name="add_product"),
    path('update-product', AdminCrudProduct.as_view(), name="update_product"),

    path('logout', LogoutView.as_view(), name="logout"),
]
