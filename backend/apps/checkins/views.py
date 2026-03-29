from rest_framework.response import Response
from rest_framework.views import APIView

from burnmap_api.predictor.logic import run_auto_check


class CheckInCreateAPIView(APIView):
    def post(self, request):
        result = run_auto_check()
        return Response(result)
