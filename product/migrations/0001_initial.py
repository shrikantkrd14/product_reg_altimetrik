# Generated by Django 4.2.11 on 2024-04-15 18:10

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
                ("code", models.CharField(max_length=5, unique=True)),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "category",
            },
        ),
        migrations.CreateModel(
            name="Supplier",
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
                ("number", models.CharField(max_length=10, unique=True)),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "supplier",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("sku", models.CharField(max_length=10, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
                ("date_of_mfg", models.DateField()),
                (
                    "warranty",
                    models.IntegerField(
                        default=None, help_text="Warranty in months", null=True
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.category",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.supplier",
                    ),
                ),
            ],
            options={
                "db_table": "product",
            },
        ),
    ]