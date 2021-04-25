from django.shortcuts import render, HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.


def show_products(request):
    products = Product.objects.all()
    return render(request, 'products/show-products.template.html', {
        'products': products
    })


def create_product(request):
    create_product_form = ProductForm()
    return render(request, 'products/create-products.template.html', {
        'form': create_product_form
    })
