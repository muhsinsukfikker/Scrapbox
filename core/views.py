from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView
from store.models import Product

class HomeView(ListView):
    model=Product
    template_name = 'home.html'
    context_object_name='products'
    queryset = Product.objects.filter(status=Product.ACTIVE)[0:8]



