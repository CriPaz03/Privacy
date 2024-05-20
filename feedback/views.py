import json

from django.http import JsonResponse
from django.shortcuts import render
from feedback.models import Feedback
from django.views.generic import ListView


# Create your views here.

'''
class FeedbackListView(ListView):
    model = Feedback
    template_name = "feedback.html"
    '''

def viewFedback(request):
    if request.method == 'GET':
        feedback = Feedback.objects.all()
        data = [
            {
                "descrizione": f.descrizione,
                "username": f.user.username
            } for f in feedback
        ]
        return JsonResponse(data)
