from rest_framework.routers import DefaultRouter

from core.views import PantsViewSet, PantsSizesViewSet

router = DefaultRouter()
router.register(r'pants', PantsViewSet)
router.register(r'pants_sizes', PantsSizesViewSet)

urlpatterns = router.urls
