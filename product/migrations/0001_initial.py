# Generated by Django 4.2.1 on 2023-05-18 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("keywords", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, upload_to="images/")),
                (
                    "status",
                    models.CharField(
                        choices=[("true", "evet"), ("false", "hayır")], max_length=10
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="product.category",
                    ),
                ),
            ],
        ),
    ]
