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
        text = data["text"] if data["text"] else ""

        pkb = Pkb.objects.filter(Q(context__in=text) | Q(strategies__in=text) | Q(description__contains=text) | Q(
            articlegdpr__article=data["article"]) | Q(owasp__top_ten=data["owasp"])).values("id", "patterns",
                                                                                            "description", "strategies")
        dict_pkb = {}
        for i in pkb:
            dict_pkb[i["id"]] = {"patterns": i["patterns"],
                                 "description": i["description"],
                                 "strategies": i["strategies"]}
        print(dict_pkb)
        return JsonResponse(dict_pkb)
