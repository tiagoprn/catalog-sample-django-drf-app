import pytest

from core.models import Pants
from core.tests.factories import PantsFactory


class TestPantApi:

    @staticmethod
    @pytest.mark.django_db
    def test_get_pants(api_client):
        pants = PantsFactory.create()

        response = api_client.get('/core/pants/')
        data = response.json()

        assert response.status_code == 200
        assert data['count'] == 1
        result = data['results'][0]
        assert result['brand'] == pants.brand
        assert result['color'] == pants.color

    @staticmethod
    @pytest.mark.django_db
    def test_get_pants_empty_list(api_client):
        response = api_client.get('/core/pants/')
        data = response.json()

        assert response.status_code == 200
        assert data['count'] == 0

    @staticmethod
    @pytest.mark.django_db
    def test_post_pants(api_client):
        payload = {
            'brand': 'Calvin Klein',
            'model': 'regular',
            'color': 'blue',
            'material': 'jeans',
            'cost_price': 24.0,
            'sell_price': 99.0,
            'taxes': 12.0
        }

        response = api_client.post(
            path='/core/pants/',
            data=payload
        )
        assert response.status_code == 201

        pants = Pants.objects.all()[0]
        for key in payload:
            assert payload[key] == getattr(pants, key)
        expected_profit = (
                payload['sell_price']
                - (payload['cost_price'] + payload['taxes'])
        )
        assert pants.profit == expected_profit
