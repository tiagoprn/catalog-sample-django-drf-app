from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from core.views import ProductViewSet, ProductSizesViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product_sizes', ProductSizesViewSet)

urlpatterns = router.urls
