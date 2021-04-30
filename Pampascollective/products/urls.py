from django.urls import path
import products.views

urlpatterns = [
    path('', products.views.show_products,
         name='show_product_route'),
    path('create', products.views.create_product),
    path('update/<product_id>',
         products.views.update_product, name='update_product_route'),
    path('delete/<product_id>',
         products.views.delete_product, name='delete_product_route'),
]
