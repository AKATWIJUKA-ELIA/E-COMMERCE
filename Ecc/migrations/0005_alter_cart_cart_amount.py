# Generated by Django 5.0.3 on 2025-01-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecc', '0004_products_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
