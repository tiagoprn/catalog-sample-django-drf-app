from rest_framework.viewsets import ModelViewSet

from core.filters import PantsFilter
from core.models import Pants
from core.pagination import StandardResultsSetPagination
from core.serializers import PantsSerializer


class PantsViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = Pants.objects.all()
    serializer_class = PantsSerializer
    pagination_class = StandardResultsSetPagination
    filterset_class = PantsFilter

    # TODO: Check if below should be enabled
    # def get_queryset(self):
    #     min_profit = self.kwargs.get('min_profit')
    #     if min_profit:
    #         self.queryset = self.queryset.filter(min_profit=min_profit)
    #     return self.queryset
