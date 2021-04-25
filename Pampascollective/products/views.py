from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.


def show_products(request):
    products = Product.objects.all()
    return render(request, 'products/show-products.template.html', {
        'products': products
    })
