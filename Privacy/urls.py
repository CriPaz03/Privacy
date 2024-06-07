"""
URL configuration for Privacy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from base.views import index
from posd.views import posdView, searchPatterns, sendNotification, exemplePatterns, posdViewAzienda, spiegazioneArticle
from feedback.views import addFeedback
from segnalazioni.views import segnalazioneView, sendSegnalazione

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", index, name="home"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('posd/', posdView, name="posd"),
    path('posd-azienda/', posdViewAzienda, name="posd_azienda"),
    path('spiegazioneArticle/<string>/', spiegazioneArticle, name="spiegazioneArticle"),
    path('search-patterns/', searchPatterns, name="search_patterns"),
    path('send-notification/<pk>/', sendNotification, name="search_patterns"),
    path('exemple-patterns/<pk>/', exemplePatterns, name="exemple_patterns"),

    path('add-feedback/', addFeedback, name="add_feedback"),

    path('segnalazione/', segnalazioneView, name="segnalazione"),
    path('valida-segnalazione/', sendSegnalazione, name="valida_segnalazione"),
]
