from django.test import TestCase
from product.usecase.product_usecase import ProductUsecase


class ProductModelTests(TestCase):

    def first_product_create_successful(self):
        input_data = {
            "sku": "21121212S",
            "name": "testing product",
            "description": "testing product desc",
            "date_of_mfg": "2024-04-10",
            "warranty": 6,
            "category": {
                "code": "SKDP",
                "name": "SKDP"
            },
            "supplier": {
                "number": "123",
                "name": "SKD Supplier"
            }
        }
        output_data = {
            "id": 1,
            "sku": "21121212S",
            "name": "testing product",
            "description": "testing product desc",
            "date_of_mfg": "2024-04-10",
            "warranty": 6,
            "category": {
                "id": 1,
                "code": "SKDP",
                "name": "SKDP"
            },
            "supplier": {
                "id": 1,
                "number": "123",
                "name": "SKD Supplier"
            }
        }
        usecase = ProductUsecase()
        serializer = usecase.upsert(input_data)
        self.assertIs(serializer.data, output_data)
