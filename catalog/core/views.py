from rest_framework.viewsets import ModelViewSet

from core.models import Pants, PantsSizes
from core.serializers import PantsSerializer, PantsSizesSerializer


class PantsViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = Pants.objects.all()
    serializer_class = PantsSerializer


class PantsSizesViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = PantsSizes.objects.all()
    serializer_class = PantsSizesSerializer

    def get_queryset(self):
        return self.queryset.filter(pants=self.kwargs['pants_pk'])
