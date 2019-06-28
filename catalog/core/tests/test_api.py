import pytest

from rest_framework.test import APITestCase

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


class TestPantApi(APITestCase):
    @pytest.mark.django_db
    def test_get_pants_when_no_pant(self):
        response = self.client.get('/core/pants/')
        response_dict = response.json()

        assert response.status_code == 200
        assert response_dict['count'] == 0
        assert get_is_paginated_with_single_page(response_dict) is True

    @pytest.mark.django_db
    def test_get_all_pants_when_single_pant(self):
        pants = PantsFactory.create()

        response = self.client.get('/core/pants/')
        response_dict = response.json()

        assert response.status_code == 200
        assert response_dict['count'] == 1

        result = response_dict['results'][0]
        assert result['brand'] == pants.brand
        assert result['color'] == pants.color

        assert get_is_paginated_with_single_page(response_dict) is True

    @pytest.mark.django_db
    def test_get_all_pants_when_should_be_paginated_with_many_pants(self):
        page_size = 5
        pants_count = 11
        _ = [PantsFactory.create() for _ in range(pants_count)]

        response = self.client.get(f'/core/pants/?page_size={page_size}')
        response_dict = response.json()

        assert response.status_code == 200
        assert response_dict['count'] == pants_count

        assert get_is_paginated_with_more_than_one_page(response_dict) is True

    @pytest.mark.django_db
    def test_get_filtered_pants_when_should_be_paginated_with_many_pants(self):
        page_size = 5
        ck_brand_count = 20
        [PantsFactory.create(brand='CK') for _ in range(ck_brand_count)]
        [PantsFactory.create(brand='TNG') for _ in range(12)]

        response = self.client.get(
            f'/core/pants/?page_size={page_size}&brand=CK'
        )
        response_dict = response.json()

        assert response.status_code == 200
        assert Pants.objects.count() == 32
        assert Pants.objects.filter(brand='CK').count() == ck_brand_count
        assert response_dict['count'] == ck_brand_count

        assert get_is_paginated_with_more_than_one_page(response_dict) is True

    @pytest.mark.django_db
    def test_post_pants_successfully(self):
        payload = {
            'brand': 'Calvin Klein',
            'model': 'regular',
            'color': 'blue',
            'material': 'jeans',
            'cost_price': 24.0,
            'sell_price': 99.0,
            'taxes': 12.0
        }

        response = self.client.post(
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

    @pytest.mark.django_db
    def test_post_pants_with_invalid_parameters(self):
        payload = {
            'brand': 'Calvin Klein',
            'model': 'regular',
            'color': 'blue',
            'cost_price': 24.0,
            'sell_price': 99.0,
            'taxes': 12.0
        }

        response = self.client.post(
            path='/core/pants/',
            data=payload
        )
        json = response.json()

        assert response.status_code == 400
        assert json == {'material': ['This field is required.']}

    @pytest.mark.django_db
    def test_put_pants_successfully(self):
        pants = PantsFactory.create()
        payload = {
            'brand': 'Calvin Klein',
            'model': 'regular',
            'color': 'blue',
            'material': 'jeans',
            'cost_price': 24.0,
            'sell_price': 99.0,
            'taxes': 12.0
        }
        database_pants = Pants.objects.get(pk=pants.id)
        assert database_pants.model != payload['model']

        response = self.client.put(
            path=f'/core/pants/{pants.id}/',
            data=payload
        )
        reloaded_pants = Pants.objects.get(pk=pants.id)
        expected_profit = (
                payload['sell_price']
                - (payload['cost_price'] + payload['taxes'])
        )

        assert response.status_code == 200
        assert reloaded_pants.profit == expected_profit
        for key in payload:
            assert payload[key] == getattr(reloaded_pants, key)

    @pytest.mark.django_db
    def test_put_pants_with_invalid_parameters(self):
        pants = PantsFactory.create()
        payload = {
            'brand': 'Calvin Klein',
            'model': 'regular',
            'color': 'blue',
            'cost_price': 24.0,
            'sell_price': 99.0,
            'taxes': 12.0
        }

        response = self.client.put(
            path=f'/core/pants/{pants.id}/',
            data=payload
        )
        json = response.json()

        assert response.status_code == 400
        assert json == {'material': ['This field is required.']}

    @pytest.mark.django_db
    def test_put_pants_not_found(self):
        payload = {
            'brand': 'Calvin Klein',
            'model': 'regular',
            'color': 'blue',
            'material': 'jeans',
            'cost_price': 24.0,
            'sell_price': 99.0,
            'taxes': 12.0
        }

        response = self.client.put(
            path=f'/core/pants/1/',
            data=payload
        )
        json = response.json()

        assert response.status_code == 404
        assert json == {'detail': 'Not found.'}

    @pytest.mark.django_db
    def test_patch_pants_successfully(self):
        pants = PantsFactory.create()
        payload = {
            'cost_price': 24.0,
            'sell_price': 99.0,
            'taxes': 12.0
        }
        database_pants = Pants.objects.get(pk=pants.id)
        assert database_pants.taxes != payload['taxes']

        response = self.client.patch(
            path=f'/core/pants/{pants.id}/',
            data=payload
        )

        reloaded_pants = Pants.objects.get(pk=pants.id)
        expected_profit = (
                payload['sell_price']
                - (payload['cost_price'] + payload['taxes'])
        )

        assert response.status_code == 200
        assert reloaded_pants.profit == expected_profit
        assert pants.color == reloaded_pants.color

    @pytest.mark.django_db
    def test_patch_pants_with_invalid_parameters(self):
        pants = PantsFactory.create()
        payload = {'brand': ''}

        response = self.client.patch(
            path=f'/core/pants/{pants.id}/',
            data=payload
        )
        json = response.json()

        assert response.status_code == 400
        assert json == {'brand': ['This field may not be blank.']}

    @pytest.mark.django_db
    def test_patch_pants_not_found(self):
        payload = {'brand': 'Calvin Klein'}

        response = self.client.patch(
            path=f'/core/pants/1/',
            data=payload
        )
        json = response.json()

        assert response.status_code == 404
        assert json == {'detail': 'Not found.'}

    @pytest.mark.django_db
    def test_delete_pants_successfully(self):
        pants = PantsFactory.create()
        assert Pants.objects.count() == 1

        response = self.client.delete(path=f'/core/pants/{pants.id}/')

        assert response.status_code == 204
        assert Pants.objects.count() == 0

    @pytest.mark.django_db
    def test_delete_pants_not_found(self):
        response = self.client.delete(path=f'/core/pants/1/')
        json = response.json()

        assert response.status_code == 404
        assert json == {'detail': 'Not found.'}
