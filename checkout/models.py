from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Purchase(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    qty = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"Purchase made for product#{self.product_id} by user#{self.user_id} on {self.purchase_date}"

    def save(self, *args, **kwargs):
        self.total = self.price * self.qty
        super().save(*args, **kwargs)
