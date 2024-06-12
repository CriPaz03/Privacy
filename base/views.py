from django.shortcuts import render
from feedback.views import get_Feedback


# Create your views here.

def index(request):
    feedback = get_Feedback()[:5]
    context = {"feedback": feedback}
    return render(request, "base.html", context)