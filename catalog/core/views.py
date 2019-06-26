from rest_framework.viewsets import ModelViewSet

from core.models import Product, ProductSizes
from core.serializers import ProductSerializer, ProductSizesSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSizesViewSet(ModelViewSet):
    queryset = ProductSizes.objects.all()
    serializer_class = ProductSizesSerializer
