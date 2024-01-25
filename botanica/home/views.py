from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import logout

def index(request):


    return render(request, "home/index.html", {})


def plant(request, plant_id : int ):
    plant = models.Plant.objects.get(id=plant_id)
    return render(request, "home/plant.html", {"plant":plant})


def logout_view(request):
    #logout the user and then render the homepage
    logout(request)
    return redirect('home')

def login_view(request):
    #redirect to the admin login page for now
    return redirect('admin:index')
def register(request):
    return "Hello world"