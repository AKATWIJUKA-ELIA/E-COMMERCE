# Generated by Django 5.0.3 on 2025-03-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecc', '0010_products_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
    ]
