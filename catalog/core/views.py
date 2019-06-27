from rest_framework.viewsets import ModelViewSet

from core.models import Pants
from core.serializers import PantsSerializer


class PantsViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = Pants.objects.all()
    serializer_class = PantsSerializer
