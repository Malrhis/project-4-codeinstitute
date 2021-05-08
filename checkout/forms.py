# Checkout/AddressForm
from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'user_id',
            'mobile',
            'postal_code',
            'address'
        )