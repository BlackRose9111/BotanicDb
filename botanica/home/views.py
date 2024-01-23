from django.shortcuts import render
from . import models
from datetime import datetime
from random import randint
# Create your views here.


def index(request):

    #query the database for a plant of the day for today, if there is not one create one for today by randomly selecting a plant
    plant_of_the_day = models.PlantOfTheDay.objects.filter(date__date=datetime.today()).first()
    if not plant_of_the_day:
        plant = list(models.Plant.objects.all())
        length = len(plant)
        if length > 0:
            random_plant = plant[randint(0,length-1)]
            plant_of_the_day = models.PlantOfTheDay.objects.create(plant=random_plant,date=datetime.today())
            plant_of_the_day.save()

    return render(request, "home/index.html", {"plant_of_the_day":plant_of_the_day})


def plant(request, plant_id : int ):
    plant = models.Plant.objects.get(id=plant_id)
    return render(request, "home/plant.html", {"plant":plant})