from django.shortcuts import render

# Create your views here.

def posdView(request):
    return render(request, "posd.html")