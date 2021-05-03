from django.shortcuts import (render,
                              reverse,
                              HttpResponse,
                              get_object_or_404)

from django.conf import settings
import stripe
import json

from products.models import Product


# Create your views here.
def checkout(request):
    # tell Stripe what my api key is
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # get shopping cart
    cart = request.session.get('shopping_cart', {})

    # create line items for checkout
    line_items = []

    # for storing the quantity of reach product
    all_product_ids = []

    for product_id, product in cart.items():
        product_model = get_object_or_404(Product, pk=product_id)

        line_item = {
            "name": product_model.name,
            "amount": int(product_model.price * 100),
            "quantity": product['qty'],
            "currency": "SGD"
        }

        line_items.append(line_item)

        all_product_ids.append({
            'product_id': product_id,
            'qty': product['qty']
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_product_ids": json.dumps(all_product_ids)
        },
        mode="payment",
        success_url=settings.STRIPE_SUCCESS_URL,
        cancel_url=settings.STRIPE_CANCEL_URL
    )

    return render(request, 'checkout/checkout-template.html', {
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })
