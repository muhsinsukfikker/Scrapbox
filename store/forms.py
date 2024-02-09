from django import forms

from .models import Product,Bid



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image','status',)


# forms.py


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount','phone_number']
