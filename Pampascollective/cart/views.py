# cart views.py
from django.shortcuts import (render,
                              redirect,
                              reverse,
                              get_object_or_404)
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):

    cart = request.session.get('shopping_cart', {})

    return render(request, 'cart/view_cart-template.html', {
        'cart': cart
    })


def add_to_cart(request, product_id):

    # retrieve shopping cart from session
    # {} is the default value if the shopping_cart is not found
    cart = request.session.get('shopping_cart', {})

    # get instance of the book model
    # criteria is product_id
    product = get_object_or_404(Product, pk=product_id)

    if product_id in cart:
        cart[product_id]['qty'] += 1

    # create cart dictionary with product_id as the key
    else:
        cart[product_id] = {
            # another dictionary
            'id': product_id,
            'name': product.name,
            'price': str(product.price),
            'qty': 1
        }

    # save the shopping cart
    request.session['shopping_cart'] = cart

    messages.success(request, (str(product.name) +
                               " has been added to cart"))
    return redirect(reverse('show_product_route'))


def remove_from_cart(request, product_id):
    # get cart from session
    cart = request.session.get('shopping_cart', {})
    product = get_object_or_404(Product, pk=product_id)

    if product_id in cart:
        # delete key from cart
        del cart[product_id]
        # save cart back into session
        request.session['shopping_cart'] = cart
        messages.success(request, (str(product.name) +
                                   " has been removed from cart"))

    return redirect(reverse('show_product_route'))
