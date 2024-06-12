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
from posd.views import posd_view, search_patterns, send_notification, exemple_patterns, posd_view_azienda, spiegazione_article, \
    privacy_by_design
from feedback.views import add_Feedback
from segnalazioni.views import segnalazioneView, sendSegnalazione

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", index, name="home"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('posd/', posd_view, name="posd"),
    path('posd-azienda/', posd_view_azienda, name="posd_azienda"),
    path('spiegazioneArticle/<string>/', spiegazione_article, name="spiegazioneArticle"),
    path('search-patterns/', search_patterns, name="search_patterns"),
    path('send-notification/<pk>/', send_notification, name="search_patterns"),
    path('exemple-patterns/<pk>/', exemple_patterns, name="exemple_patterns"),
    path('privacy-by-design/<pk>/', privacy_by_design, name="exemple_patterns"),

    path('add-feedback/', add_Feedback, name="add_feedback"),

    path('segnalazione/', segnalazioneView, name="segnalazione"),
    path('valida-segnalazione/', sendSegnalazione, name="valida_segnalazione"),
]
