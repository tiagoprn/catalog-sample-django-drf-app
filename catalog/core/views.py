from rest_framework.viewsets import ModelViewSet

from core.models import Pants, PantsSizes
from core.serializers import PantsSerializer, PantsSizesSerializer


class PantsViewSet(ModelViewSet):
    queryset = Pants.objects.all()
    serializer_class = PantsSerializer


class PantsSizesViewSet(ModelViewSet):
    queryset = PantsSizes.objects.all()
    serializer_class = PantsSizesSerializer
