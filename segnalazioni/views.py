import json

from django.http import JsonResponse
from django.shortcuts import render

from segnalazioni.models import Seganalazione


# Create your views here.
def segnalazioneView(request):
    return render(request, "segnalazioni.html")

def sendSegnalazione(request):
    if request.method == "POST":
        query_string = request.body.decode('utf-8')
        if request.user.is_authenticated:
            start = query_string.find("message=") + len("message=")

            # Trova la fine del valore di 'message'
            end = query_string.find("&", start)
            if end == -1:  # Se non c'è un altro parametro dopo 'message'
                end = len(query_string)

            # Estrarre il valore di 'message'
            message_value = query_string[start:end]
            Seganalazione.objects.create(
                user=request.user,
                description=message_value
            )
            return JsonResponse({"success": True})
    return JsonResponse({"success": False})
