from rest_framework.serializers import ModelSerializer

from apps.task3.models import Product

from apps.task3.utils import encrypt


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'marja', 'package_code')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        title = representation.get('title')
        price = representation.get('price')
        marja = representation.get('marja')
        package_code = representation.get('package_code')

        representation["title"] = encrypt(title)
        representation["price"] = encrypt(price)
        representation["marja"] = encrypt(marja)
        representation["package_code"] = encrypt(package_code)

        return representation
