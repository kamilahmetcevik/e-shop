# Generated by Django 4.2.1 on 2023-06-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0005_order_total_currency_alter_order_country_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="total_currency",
        ),
        migrations.AlterField(
            model_name="order",
            name="total",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
