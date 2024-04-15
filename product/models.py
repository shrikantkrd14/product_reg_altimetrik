from django.db import models


class Supplier(models.Model):
    number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "supplier"


class Category(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "category"


class Product(models.Model):
    sku = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_of_mfg = models.DateField()
    warranty = models.IntegerField(help_text="Warranty in months", null=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"




