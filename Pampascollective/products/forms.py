from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'price_in_cents',
            'colour',
            'length',
            'desc'
        )
