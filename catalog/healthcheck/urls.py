from django.conf.urls import url

from healthcheck.views import HealthCheckView

urlpatterns = [
    url(
        r'^$',
        HealthCheckView.as_view(),
        name='status'
    )
]
