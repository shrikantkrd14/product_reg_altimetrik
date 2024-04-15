from django.urls import path
from product.views import ProductView

urlpatterns = [
    path(r'', ProductView.as_view()),
    path(r'<int:product_id>/', ProductView.as_view()),
]
