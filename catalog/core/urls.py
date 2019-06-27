from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from core.views import PantsViewSet

router = routers.SimpleRouter()
router.register(r'pants', PantsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
