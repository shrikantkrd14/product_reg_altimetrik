from django.db import transaction
from django.db.models import Q

from datetime import datetime
from product.models import Product, Supplier, Category
from product.serializer import ProductSerializer


class ProductUsecase:

    @transaction.atomic
    def upsert(self, data):
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        supplier_detail = data.pop("supplier")
        category_detail = data.pop("category")
        supplier = Supplier.objects.filter(number=supplier_detail["number"]).first()
        if not supplier:
            supplier = Supplier(
                number = supplier_detail["number"]
            )
        supplier.name = supplier_detail["name"]

        category = Category.objects.filter(code=category_detail["code"]).first()
        if not category:
            category = Category(
                code = category_detail["code"]
            )
        category.name = category_detail["name"]

        product = Product.objects.filter(sku=data["sku"]).first()
        if not product:
            product = Product(
                sku=data["sku"],
            )
        product.name = data["name"]
        product.description = data["description"]
        product.date_of_mfg = datetime.strptime(data["date_of_mfg"], '%Y-%m-%d').date()
        product.warranty = data["warranty"]
        product.category = category
        product.supplier = supplier

        supplier.save()
        category.save()
        product.save()

        return ProductSerializer(instance=product)

    def search(self, keyword):

        queryset = Q(sku__icontains=keyword) | Q(name__icontains=keyword) | Q(category__code__icontains=keyword) | \
                   Q(supplier__number__icontains=keyword)
        return ProductSerializer(list(Product.objects.filter(queryset)), many=True)
