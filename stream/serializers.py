from rest_framework import serializers

from authentication.serializers import SimpleUserSerializer
from stream.models import StreamProfile


class StreamProfileSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()

    class Meta:
        model = StreamProfile
        fields = [
            "id",
            "user",
            "url",
            "title",
            "description",
            "is_streaming",
            "viewers",
        ]
