from rest_framework.test import APITestCase


class TestHealthCheckView(APITestCase):  # pylint: disable=too-many-ancestors

    def test_status(self):
        response = self.client.get('/healthcheck/')
        assert response.status_code == 200
