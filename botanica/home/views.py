from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    return render(request, "home/index.html")


def plant(request, plant_id : int ):
    plant = models.Plant.objects.get(id=plant_id)
    return render(request, "home/plant.html", {"plant":plant})