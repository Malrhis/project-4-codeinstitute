from django import forms
from .models import Product, ProductType, Colour, Tag


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'product_type',
            'price',
            'colour',
            'tag',
            'length',
            'desc',
            'quantity'
        )
