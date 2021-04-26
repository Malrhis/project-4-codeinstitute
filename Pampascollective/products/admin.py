from django.contrib import admin
from .models import Product, ProductType, Colour

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Colour)
