import json

from django.http import JsonResponse
from django.shortcuts import render
from feedback.models import Feedback
from django.views.generic import ListView


# Create your views here.

def getFeedback():
    feedback = Feedback.objects.all()
    data = [
        {
            "descrizione": f.descrizione,
            "username": f.user.username,
        } for f in feedback
    ]
    return data

def addFeedback(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            json_data = json.loads(request.body, encoding='utf-8')
            print(json_data)
        else:
            return JsonResponse({"error": "User is not authenticated"}, status=400)

