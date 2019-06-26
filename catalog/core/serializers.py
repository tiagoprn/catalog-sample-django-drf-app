from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from core.models import Product, ProductSizes


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSizesSerializer(ModelSerializer):
    # below is just to show on GET method
    product = ProductSerializer(read_only=True)

    # below is to support writing to montadora_id on POST, PUT, PATCH, DELETE
    product_id = PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = ProductSizes
        fields = ('id', 'size', 'product', 'product_id',
                  'is_active', 'created', 'updated')
