# Generated by Django 4.2.1 on 2023-06-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0013_product_price_currency_alter_product_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="price_currency",
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
