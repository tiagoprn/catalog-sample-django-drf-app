from rest_framework.serializers import ModelSerializer

from core.models import Pants, PantsSizes


class PantsSizesSerializer(ModelSerializer):  # pylint: disable=too-many-ancestors
    class Meta:
        model = PantsSizes
        fields = ('size', 'created', 'updated')


class PantsSerializer(ModelSerializer):  # pylint: disable=too-many-ancestors
    pants_sizes = PantsSizesSerializer(many=True, read_only=True)

    class Meta:
        model = Pants
        fields = (
            'id', 'brand', 'model', 'color', 'material', 'cost_price',
            'sell_price', 'profit', 'taxes', 'is_active', 'created', 'updated',
            'pants_sizes'
        )
