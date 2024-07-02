from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.shortcuts import HttpResponseRedirect, render
from django.views.decorators.http import require_http_methods

from accounts.forms import FormRegistrazione


@require_http_methods(["GET", "POST"])
def registrazione_view(request):
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            groups = form.cleaned_data["groups"]
            user = User.objects.create_user(username=username, password=password, email=email)
            groups.last().user_set.add(user)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = FormRegistrazione()
    context = {"form": form}
    return render(request, "accounts/registrazione.html", context)


