from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheckView(APIView):

    permission_classes = ()

    def get(self, request):
        return Response()
