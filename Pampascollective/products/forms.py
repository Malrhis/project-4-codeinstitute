# ProductForm
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


# normal form
class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    product_type = forms.ModelChoiceField(
        queryset=ProductType.objects.all(), required=False)
