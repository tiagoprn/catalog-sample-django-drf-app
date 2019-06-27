from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
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


class CSVImportView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, format='csv'):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                data={'message': 'No file uploaded.'}
            )
        # do some stuff with uploaded file
        lines = []
        for line in file_obj.readlines():
            lines.append(line)

        return Response(
            status=status.HTTP_200_OK,  # Change to http 204
            data={'contents': lines}
        )
