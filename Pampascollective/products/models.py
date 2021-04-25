from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(blank=False, max_length=255)
    price_in_cents = models.IntegerField(blank=False)
    colour = models.CharField(blank=False, max_length=45)
    length = models.FloatField(blank=False)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name
