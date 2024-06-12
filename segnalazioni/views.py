import json

from django.http import JsonResponse
from django.shortcuts import render

from segnalazioni.models import Seganalazione


# Create your views here.
def segnalazioneView(request):
    return render(request, "segnalazioni.html")

def sendSegnalazione(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            json_str = request.body.decode('utf-8')
            Seganalazione.objects.create(
                user=request.user,
                description=json_str.replace(f"username={request.user.username}&message=", "")
            )
            return JsonResponse({"success": True})
    return JsonResponse({"success": False})
