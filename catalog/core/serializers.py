from rest_framework.serializers import ModelSerializer

from core.models import Pants


class PantsSerializer(ModelSerializer):  # pylint: disable=too-many-ancestors
    class Meta:
        model = Pants
        fields = (
            'brand', 'model', 'color', 'material',
            'cost_price', 'sell_price', 'taxes'
        )
