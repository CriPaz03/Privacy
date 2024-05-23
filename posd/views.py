import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from posd.models import *


# Create your views here.

def posdView(request):
    article = ArticleGdpr.Article.choices
    owasp = Owasp.TopTen.choices
    context = {'article': article, 'owasp': owasp}
    return render(request, "posd.html", context)


def searchPatterns(request):
    if request.method == "POST":
        json_str = request.body.decode('utf-8')
        data = json.loads(json_str)
        text = data["text"] if data["text"] else None
        if text:
            pkb_context = Pkb.objects.filter(context__in=text)
            pkb_description = Pkb.objects.filter(description__contains=text)

        pkb_articlegdpr = Pkb.objects.filter(articlegdpr__article=data["article"])
        pkb_owasp = Pkb.objects.filter(owasp__top_ten=data["owasp"])

        if text:
            pkb = pkb_articlegdpr | pkb_owasp | pkb_description | pkb_context
        else:
            pkb = pkb_articlegdpr | pkb_owasp
        pkb = pkb.values("id", "patterns", "description", "strategies")
        dict_pkb = {}
        for i in pkb:
            dict_pkb[i["id"]] = {"patterns": i["patterns"],
                                 "description": i["description"],
                                 "strategies": i["strategies"]}
        return JsonResponse(dict_pkb)
