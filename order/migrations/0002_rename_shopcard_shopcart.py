# Generated by Django 4.2.1 on 2023-06-08 17:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0011_alter_comment_options"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ShopCard",
            new_name="ShopCart",
        ),
    ]
