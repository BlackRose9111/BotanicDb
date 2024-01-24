from django.shortcuts import render
from . import models
from datetime import datetime
from random import randint
# Create your views here.


def index(request):

    #query the database for a plant of the day for today, if there is not one create one for today by randomly selecting a plant

    return render(request, "home/index.html", {})


def plant(request, plant_id : int ):
    plant = models.Plant.objects.get(id=plant_id)
    return render(request, "home/plant.html", {"plant":plant})