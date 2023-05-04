from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from stream.models import StreamProfile


class VerifyStreamKey(APIView):
    permission_classes = []

    def post(self, request):
        stream_key = request.data.get("stream")

        if not StreamProfile.objects.filter(stream_key=stream_key).exists():
            return JsonResponse(
                {
                    "code": 1,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return JsonResponse(
            {
                "code": 0,
            }
        )
