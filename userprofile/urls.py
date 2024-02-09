from django.urls import path
from .views import  VendorDetailView,RegisterView,LogoutView,MyAccountView,MyStoreView
from django.contrib.auth import views as auth_views
from store.views import AddProductView,ProductUpdateView,DeleteProductView
# from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('vendor/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),



    path('myaccount/', MyAccountView.as_view(), name='myaccount'),
    path('mystore/', MyStoreView.as_view(), name='mystore'),
    path('mystore/add/',AddProductView.as_view(), name='add'),
    path('mystore/edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit-product'),
    path('mystore/delete_product/<int:pk>/', DeleteProductView.as_view(), name='delete-product'),




   
]
