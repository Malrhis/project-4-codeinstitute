from django.urls import path

from .views import checkout, payment_completed,  checkout_success

urlpatterns = [
    path('', checkout, name='checkout'),
    path('success', checkout_success, name="checkout_success"),
    # path('success', checkout_cancelled, name="checkout_cancelled"),
    path('payment_completed', payment_completed)
]
