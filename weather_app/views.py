from django.shortcuts import render

from .weather import *


def index(request):
    return render(request, "weather_app/index.html")
