from django.shortcuts import (render,
                              reverse,
                              HttpResponse,
                              get_object_or_404)
# import settings so that we can access the public stripe key
from django.conf import settings
import stripe
import json

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from products.models import Product
from checkout.models import Purchase

from django.contrib.sites.models import Site

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required
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
        # retrieve the book by its id from the database
        product_model = get_object_or_404(Product, pk=product_id)

        # create line item
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

    # get the current website
    current_site = Site.objects.get_current()

    # get the domain name
    domain = current_site.domain

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


@login_required
def checkout_success(request):
    # Empty the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Checkout success")


@login_required
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")


# exempt from CSRF so that stripe can call our endpoint
@csrf_exempt
def payment_completed(request):
    # verify that request is from stripe
    payload = request.body

    # extract signature
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    # prepare variable to store data that stripe is sending
    event = None

    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature - data is not from stripe
        return HttpResponse(status=400)

    # once we have verified from Stripe, we extract data
    # check if the event type is checkout.session.completed
    if event['type'] == 'checkout.session.completed':

        # if yes, then event represents that payment session is completed
        session = event['data']['object']

        # call handle_payment function to handle the payment complete
        print(session)
        # handle_payment(session)
        request.session['shopping_cart'] = {}
        print(request.session['shopping_cart'])

    return HttpResponse(status=200)


def handle_payment(session):
    user = get_object_or_404(User, pk=session["client_reference_id"])

    # change the metadata from string back to array
    all_product_ids_str = session["metadata"]["all_product_ids"]
    all_product_ids = json.loads(all_product_ids_str)
    # go through each book id
    for product_id in all_product_ids:
        product_model = get_object_or_404(Product, pk=product_id)

        # create the purchase model
        purchase = Purchase()
        purchase.product_id = product_model
        purchase.user_id = user
        purchase.save()
