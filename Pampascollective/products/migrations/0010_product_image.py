# Generated by Django 3.2 on 2021-05-02 04:15

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_tags_product_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
