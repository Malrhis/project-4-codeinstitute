from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.


def show_products(request):
    products = Product.objects.all()
    return render(request, 'products/show-products.template.html', {
        'products': products
    })


def create_product(request):
    if request.method == 'POST':
        create_product_form = ProductForm(request.POST)

        if create_product_form.is_valid():
            create_product_form.save()
            return redirect(reverse(show_products))
        else:
            return render(request, 'products/create-products.template.html', {
                'form': create_product_form
            })

    else:
        create_product_form = ProductForm()
        return render(request, 'products/create-products.template.html', {
            'form': create_product_form
        })


