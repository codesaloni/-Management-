# forms.py
from django import forms
from .models import Product,staff,Seller

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']

class staffForm(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['staff_name', 'staff_number', 'staff_email']


class sellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['seller_name', 'seller_email', 'seller_address','seller_number','seller_quantity']
