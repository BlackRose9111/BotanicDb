from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import logout
#import request
from django.http import HttpRequest

def index(request : HttpRequest):

    all_plants = list(models.Plant.objects.all())
    all_plants2 = [ all_plants[0] for i in range(0, 50)]

    return render(request, "home/index.html", {"plants": all_plants2})


def plant(request):
    plant_id = request.GET.get("plant_id")

    plant = models.Plant.objects.get(id=plant_id)


    return render(request, "home/plant.html", {"plant":plant,"page" : "Plant"})


def logout_view(request):
    #logout the user and then render the homepage
    logout(request)
    #return to the current page
    return redirect(request.META['HTTP_REFERER'])

def login_view(request):
    #redirect to the admin login page for now
    return redirect('admin:index')
def register(request):
    return "Hello world"

def search(request):


    return render(request, "home/search.html", {"plants":plants})


