from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,View,ListView,CreateView,UpdateView
from .models import Product,Category,Bid
from .forms import ProductForm,BidForm
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    


class CategoryDetailView(View):
    template_name = 'category_detail.html'

    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        products = category.products.filter(status=Product.ACTIVE)

        context = {
            'category': category,
            'products': products
        }

        return render(request, self.template_name, context)
    

class ProductView(ListView):
    model = Product
    template_name='shop.html'
    context_object_name='products'
    queryset = Product.objects.filter(status=Product.ACTIVE)




class SearchView(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        products = Product.objects.filter(status=Product.ACTIVE).filter(title__icontains=query)

        context = {
            'query': query,
            'products': products,
        }

        return render(request, self.template_name, context)




class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('mystore')
    extra_context = {'title': 'Add'}

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.title)
        messages.success(self.request, 'The product was added!')
        return super().form_valid(form)
    

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'  # Set your template path
    success_url = reverse_lazy('mystore')
    extra_context = {'title': 'Edit'}
    context_object_name = 'product'
    

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'The changes were saved!')
        return super().form_valid(form)


class DeleteProductView(View): 

    def get(self, request, pk):
        product = Product.objects.filter(user=request.user).get(pk=pk)
        product.status = Product.DELETED
        product.save()

        messages.success(request, 'The product was deleted!')

        return redirect('mystore')
    

class CreateBidView(LoginRequiredMixin,CreateView):
    model = Bid
    form_class = BidForm
    template_name = 'create_bid.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.bidder = self.request.user
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)