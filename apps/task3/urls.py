from django.urls import path

from apps.task3.api_endpoints import product

urlpatterns = [
    path("product-list/", product.ProductListAPIView.as_view(), name="product-list"),
]

