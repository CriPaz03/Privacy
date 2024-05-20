import json

from django.http import JsonResponse
from django.shortcuts import render
from feedback.models import Feedback
from django.views.generic import ListView


# Create your views here.

'''
class viewFedback(ListView):
    model = Feedback
    template_name = "feedback.html"
    '''

def getFeedback():
    feedback = Feedback.objects.all()
    data = [
        {
            "descrizione": f.descrizione,
            "username": f.user.username
        } for f in feedback
    ]
    return data
