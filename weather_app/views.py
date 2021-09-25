from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import CityWeather
from .weather import one_call_weather, city_weather_call
from .forms import CityForm


# def index(request):
#     return render(request, "weather_app/index.html")


class HomeWeather(ListView):
    model = CityWeather
    template_name = "/weather_app/index.html"
    context_object_name = "forecasts"


class AddCity(CreateView):
    form_class = CityForm
