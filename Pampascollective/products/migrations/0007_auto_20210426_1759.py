# Generated by Django 3.2 on 2021-04-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210426_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_in_cents',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
