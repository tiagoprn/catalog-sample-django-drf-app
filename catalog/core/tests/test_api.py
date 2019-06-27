import pytest

from core.models import Pants
from core.tests.factories import PantsFactory


def get_is_paginated_with_more_than_one_page(response_dict):
    has_pagination_params = True
    for param in ['page', 'page_size']:
        if param not in response_dict['next']:
            return False

    has_pagination_keys = {'next', 'previous'}.intersection(
        set(response_dict.keys()))

    return has_pagination_keys and has_pagination_params


def get_is_paginated_with_single_page(response_dict):
    has_pagination_keys = {'next', 'previous'}.intersection(
        set(response_dict.keys()))

    no_previous_and_next_pages = (
            response_dict['next'] is None
            and response_dict['previous'] is None
    )

    return has_pagination_keys and no_previous_and_next_pages


class TestPantApi:
    @staticmethod
    @pytest.mark.django_db
    def test_get_pants_when_no_pant(api_client):
        response = api_client.get('/core/pants/')
        response_dict = response.json()

        assert response.status_code == 200
        assert response_dict['count'] == 0
        assert get_is_paginated_with_single_page(response_dict) is True

    @staticmethod
    @pytest.mark.django_db
    def test_get_all_pants_when_single_pant(api_client):
        pants = PantsFactory.create()

        response = api_client.get('/core/pants/')
        response_dict = response.json()

        assert response.status_code == 200
        assert response_dict['count'] == 1

        result = response_dict['results'][0]
        assert result['brand'] == pants.brand
        assert result['color'] == pants.color

        assert get_is_paginated_with_single_page(response_dict) is True

    @staticmethod
    @pytest.mark.django_db
    def test_get_all_pants_when_should_be_paginated_with_many_pants(api_client):
        page_size = 5
        pants_count = 11
        _ = [PantsFactory.create() for _ in range(pants_count)]

        response = api_client.get(f'/core/pants/?page_size={page_size}')
        response_dict = response.json()

        assert response.status_code == 200
        assert response_dict['count'] == pants_count

        assert get_is_paginated_with_more_than_one_page(response_dict) is True

    @staticmethod
    @pytest.mark.django_db
    def test_post_pants_successfully(api_client):
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
