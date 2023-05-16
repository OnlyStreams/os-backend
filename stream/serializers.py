from rest_framework import serializers

from authentication.serializers import SimpleUserSerializer
from stream.models import StreamProfile


class StreamProfileSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()
    url = serializers.CharField(source="get_url")

    class Meta:
        model = StreamProfile
        fields = [
            "id",
            "url",
            "user",
            "title",
            "description",
            "is_streaming",
            "viewers",
        ]
