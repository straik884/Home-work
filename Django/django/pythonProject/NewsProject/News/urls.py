from django.contrib import admin
from django.urls import path

from News.views import hello


urlpatterns = [
    path('', hello),
]
