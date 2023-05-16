from django.http import JsonResponse
from rest_framework import permissions, status, viewsets
from rest_framework.views import APIView

from stream.models import StreamProfile
from stream.serializers import StreamProfileSerializer


class StreamViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = StreamProfileSerializer
    queryset = StreamProfile.objects.filter(is_streaming=True)


class StreamModifyView(APIView):
    def post(self, request):
        user = request.user

        try:
            stream_profile = user.streamprofile
        except StreamProfile.DoesNotExist:
            return JsonResponse({"detail": "You do not have a stream profile. Add it via Django admin."}, status=404)

        url = request.data.get("url", None)
        title = request.data.get("title", None)
        description = request.data.get("description", None)
        is_streaming = request.data.get("is_streaming", None)
        viewers = request.data.get("viewers", None)

        if url is not None:
            stream_profile.url = url

        if title is not None:
            stream_profile.title = title

        if description is not None:
            stream_profile.description = description

        if is_streaming is not None:
            stream_profile.is_streaming = is_streaming

        if viewers is not None:
            stream_profile.viewers = viewers

        stream_profile.save()

        return JsonResponse(StreamProfileSerializer(stream_profile).data)


class VerifyStreamKeyView(APIView):
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


class GetStreamKeyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return JsonResponse(
            {
                "stream_key": request.user.streamprofile.stream_key,
            }
        )


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return JsonResponse(StreamProfileSerializer(request.user.streamprofile).data)
