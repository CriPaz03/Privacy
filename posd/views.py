import json

import openai

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from Privacy.settings import GPT_KEY
from posd.models import ArticleGdpr, Owasp, Pkb, Notification, Example, PrivacyByDesign


# Create your views here.

@require_http_methods(["GET", "POST"])
def posd_view(request):
    article = ArticleGdpr.Article.choices
    owasp = Owasp.TopTen.choices
    context = {'article': article, 'owasp': owasp}
    return render(request, "posd.html", context)


@require_http_methods(["POST"])
def search_patterns(request):
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


@require_http_methods(["GET"])
def send_notification(request, pk):
    if request.method == "GET":
        pkb = Pkb.objects.get(pk=pk)
        Notification.objects.create(pkb=pkb, user=request.user)
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})


@require_http_methods(["GET"])
def exemple_patterns(request, pk):
    if request.method == "GET":
        exemple = Example.objects.filter(pkb_id=pk).values("id", "example")
        dict_exemple = {}
        for i in exemple:
            dict_exemple.setdefault(i["id"], []).append(i["example"])
        return JsonResponse({"success": True, "exemple": dict_exemple})


@require_http_methods(["GET"])
def privacy_by_design(request, pk):
    if request.method == "GET":
        design = PrivacyByDesign.objects.filter(pkb_id=pk).values("id", "design")
        dict_exemple = {}
        for i in design:
            for choice in PrivacyByDesign.Design.choices:
                if choice[0] == i["design"]:
                    dict_exemple.setdefault(i["id"], []).append(choice[1])

        return JsonResponse({"success": True, "privacy": dict_exemple})
    return JsonResponse({"success": False})


@require_http_methods(["GET"])
def posd_view_azienda(request):
    article = ArticleGdpr.Article.choices
    context = {'article': article, 'patterns': Pkb.objects.all()}
    return render(request, "azienda.html", context)


@require_http_methods(["GET"])
def spiegazione_article(request, string):
    if request.method == "GET":
        article = ArticleGdpr.Article(string).label
        openai.api_key = GPT_KEY
        stream = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Mi spieghi questo articolo del gdpr ${article}"}],
        )

        return JsonResponse({"success": True, "response": str(stream.chois[0].message.content)})
    return JsonResponse({"success": False})
