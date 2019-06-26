from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from core.models import Pants, PantsSizes


class PantsSerializer(ModelSerializer):
    class Meta:
        model = Pants
        fields = '__all__'


class PantsSizesSerializer(ModelSerializer):
    # below is just to show on GET method
    pants = PantsSerializer(read_only=True)

    # below is to support writing to montadora_id on POST, PUT, PATCH, DELETE
    pants_id = PrimaryKeyRelatedField(
        queryset=Pants.objects.all(), source='pants', write_only=True)

    class Meta:
        model = PantsSizes
        fields = ('id', 'size', 'pants', 'pants_id',
                  'is_active', 'created', 'updated')
