from django.urls import reverse as r


class TestHealthCheckView:

    def test_status(self, api_client):
        url = r('healthcheck:status')
        response = api_client.get(url)
        assert response.status_code == 200
