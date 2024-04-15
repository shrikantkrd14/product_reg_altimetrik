import ujson
from django.views import View

from product.models import Product
from product.serializer import ProductSerializer
from product.usecase.product_usecase import ProductUsecase
from product_reg_altimetrik.response import Response


class ProductView(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usecase = ProductUsecase()

    def post(self, request):
        data = ujson.loads(request.body)
        serializer = self.usecase.upsert(data)
        return Response(data=serializer.data)

    def put(self, request, product_id):
        data = ujson.loads(request.body)
        serializer = self.usecase.upsert(data)
        return Response(data=serializer.data)

    def get(self, request, product_id=None):
        if product_id:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(instance=product)
        else:
            search_keyword = request.GET.get('search', '')
            serializer = self.usecase.search(search_keyword)
        return Response(data=serializer.data)

    def delete(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response()
