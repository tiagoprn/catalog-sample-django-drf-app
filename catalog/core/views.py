from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.business import import_csv
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

    @staticmethod
    def post(request, format='csv'):  # pylint: disable=redefined-builtin, unused-argument
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                data={'message': 'No file uploaded.'}
            )
        # do some stuff with uploaded file
        result = import_csv(file_obj)

        if result['successful_imports'] > 0:
            response_status = status.HTTP_200_OK
        else:
            response_status = status.HTTP_422_UNPROCESSABLE_ENTITY

        return Response(
            status=response_status,
            data=result
        )
