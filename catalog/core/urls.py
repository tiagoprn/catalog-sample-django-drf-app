from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from core.views import PantsViewSet, PantsSizesViewSet

router = routers.SimpleRouter()
router.register(r'pants', PantsViewSet)

pants_router = routers.NestedSimpleRouter(router, r'pants', lookup='pants')
pants_router.register(r'pants_sizes', PantsSizesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(pants_router.urls))
]
