from rest_framework.response import Response
from rest_framework.views import APIView

from core.settings import API_SETTINGS


class ApiIndexView(APIView):
    permission_classes = []

    def get(self, request):
        return Response(
            {
                "name": API_SETTINGS["NAME"],
                "description": API_SETTINGS["DESCRIPTION"],
                "url": API_SETTINGS["URL"],
                "version": API_SETTINGS["VERSION"],
                "authors": API_SETTINGS["AUTHORS"],
            }
        )
