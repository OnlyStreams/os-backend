from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.views import APIView


class BalanceView(APIView):
    def get(self, request):
        return JsonResponse(
            {
                "balance": request.user.tokenprofile.balance,
            }
        )


class TipView(APIView):
    def post(self, request):
        streamer_id = request.data.get("streamer_id", None)
        amount = request.data.get("amount", None)

        if streamer_id is None:
            return JsonResponse({"detail": "streamer_id not provided"}, status=400)

        if amount is None:
            return JsonResponse({"detail": "amount not provided"}, status=400)

        try:
            streamer = User.objects.get(id=streamer_id)
        except User.DoesNotExist:
            return JsonResponse({"detail": "that streamer does not exist"}, status=400)

        if request.user.tokenprofile.balance < amount:
            return JsonResponse({"detail": "you broke, add funds before trying to tip"}, status=400)

        if amount <= 0:
            return JsonResponse({"detail": "amount needs to be greater than 0"}, status=400)

        streamer.tokenprofile.balance += amount
        streamer.tokenprofile.save()

        request.user.tokenprofile.balance -= amount
        request.user.tokenprofile.save()

        return JsonResponse(
            {
                "detail": "you've successfully tipped! thanks for supporting the streamers. uwu :3",
            }
        )
