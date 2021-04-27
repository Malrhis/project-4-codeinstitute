"""Pampascollective URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import products.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', products.views.show_products,
         name='show_product_route'),
    path('products/create', products.views.create_product),
    path('products/update/<product_id>',
         products.views.update_product, name='update_product_route'),
    path('products/delete/<product_id>',
         products.views.delete_product, name='delete_product_route'),
    path('reviews/', reviews.views.show_reviews)
]
