from rest_framework.test import APITestCase


class TestHealthCheckView(APITestCase):

    def test_status(self):
        response = self.client.get('/healthcheck/')
        assert response.status_code == 200
