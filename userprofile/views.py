from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.views.generic import View,TemplateView
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth import logout
from store.models import Product,Bid
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserUpdateForm, ProfileUpdateForm


# Create your views here.


class VendorDetailView(View):
    template_name = 'vendor_detail.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        profile = Profile.objects.get(user=user)  # Get the profile associated with the user
        products = user.products.filter(status=Product.ACTIVE)
        total_product_count = products.count()

        return render(request, self.template_name, {
            'user': user,
            'products': products,
            'total_product_count': total_product_count,
            'profile':profile  

        })
   

    

 

class RegisterView(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()  # Save the user instance
            # Create a UserProfile instance for the new user
            # Profile.objects.create(user=user)           
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        return render(request, self.template_name, {'form': form})


class MyAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'myaccount.html'

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('myaccount')
        return render(request, self.template_name, {'u_form': u_form, 'p_form': p_form})

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, self.template_name, {'u_form': u_form, 'p_form': p_form})

class MyStoreView(LoginRequiredMixin, View):
    template_name = 'mystore.html'

    def get(self, request):
        products = request.user.products.exclude(status=Product.DELETED)
        for product in products:
            product.bids = product.bid_set.all()
            print(product.bids)
            # Fetch all bids associated with each product
        return render(request, self.template_name, {
            'products': products,
        })



class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        # Redirect to a specific page after logout
        return redirect('home')