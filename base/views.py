from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from feedback.views import get_Feedback


# Create your views here.

@require_http_methods(["GET"])
def index(request):
    feedback = get_Feedback()
    context = {"feedback": feedback}
    return render(request, "base.html", context)