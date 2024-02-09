from django.urls import path
from .views import  ProductDetailView,CategoryDetailView,ProductView,SearchView,AddProductView,CreateBidView

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),

    path('product/<slug:category_slug>/<slug:slug>/',ProductDetailView.as_view(),name='product-detail'),
    path('shop',ProductView.as_view(), name='shop'),
    path('search/', SearchView.as_view(), name='search'),
    path('bid/product/<int:pk>', CreateBidView.as_view(), name='create_bid'),
   
]
