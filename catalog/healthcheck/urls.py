from django.conf.urls import url

from .views import HealthCheckView

urlpatterns = [
    url(
        r'^$',
        HealthCheckView.as_view(),
        name='status'
    )
]
