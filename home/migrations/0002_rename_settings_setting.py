# Generated by Django 4.2.1 on 2023-05-19 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Settings",
            new_name="Setting",
        ),
    ]