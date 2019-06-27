from rest_framework.viewsets import ModelViewSet

from core.models import Pants
from core.pagination import StandardResultsSetPagination
from core.serializers import PantsSerializer


class PantsViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = Pants.objects.all()
    serializer_class = PantsSerializer
    pagination_class = StandardResultsSetPagination
