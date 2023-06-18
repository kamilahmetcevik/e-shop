# Generated by Django 4.2.1 on 2023-06-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_order_orderproduct"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("New", "New"),
                    ("Accepted", "Accepted"),
                    ("Preaparing", "Preaparing"),
                    ("Onshipping", "Onshipping"),
                    ("Completed", "Completed"),
                    ("Canceled", "Canceled"),
                ],
                default="New",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="total",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
