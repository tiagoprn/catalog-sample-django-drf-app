from rest_framework.routers import DefaultRouter

from core.views import PantsViewSet

router = DefaultRouter()
router.register(r'pants', PantsViewSet)

urlpatterns = router.urls
