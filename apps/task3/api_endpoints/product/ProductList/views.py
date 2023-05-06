from rest_framework.generics import ListAPIView

from .serializers import ProductListSerializer

from apps.task3.models import Product


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()