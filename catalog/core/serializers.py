from rest_framework.serializers import ModelSerializer

from core.models import Pants


class PantsSerializer(ModelSerializer):  # pylint: disable=too-many-ancestors
    class Meta:
        model = Pants
        fields = (
            'id', 'brand', 'model', 'color', 'material', 'cost_price',
            'sell_price', 'profit', 'taxes', 'created', 'updated'
        )
