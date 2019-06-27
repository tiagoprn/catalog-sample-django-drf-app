from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from core.views import PantsViewSet, CSVImportView

router = DefaultRouter()
router.register(r'pants', PantsViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(
        r'^csv_import$',
        CSVImportView.as_view(),
        name='csv_import'
    )
]
