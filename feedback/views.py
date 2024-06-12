import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from feedback.models import Feedback
from django.views.generic import ListView


# Create your views here.

def get_Feedback():
    feedback = Feedback.objects.all()
    data = [
        {
            "descrizione": f.descrizione,
            "username": f.user.username,
        } for f in feedback
    ]
    return data


@require_http_methods(["POST"])
def add_Feedback(request):

    if request.method == "POST":
        json_str = request.body.decode('utf-8')
        description = json_str.replace(f"username={request.user.username}&message=", "")
        Feedback.objects.create(user=request.user, descrizione=description.replace("+", " "))
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

