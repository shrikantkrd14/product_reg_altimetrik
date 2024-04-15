from rest_framework import serializers
from product.models import Product, Supplier, Category


class SupplierSerializer(serializers.ModelSerializer):
    number = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Supplier
        fields = ("id","number", "name")


class CategorySerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=5)
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = ("id", "code", "name")


class ProductSerializer(serializers.ModelSerializer):

    sku = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    date_of_mfg = serializers.DateField()
    warranty = serializers.IntegerField(allow_null=True, default=None)
    category = CategorySerializer(help_text="Product Category")
    supplier = SupplierSerializer(help_text="Product Manufacturer")

    class Meta:
        model = Product
        fields = ("id", "sku", "name", "description", "date_of_mfg", "warranty", "category", "supplier")



