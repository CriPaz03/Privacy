from django.shortcuts import render
from base.models import *
from feedback.models import Feedback
from feedback.views import getFeedback


# Create your views here.

def index(request):
    feedback = getFeedback()
    context = {"feedback": feedback}
    return render(request, "base.html", context)