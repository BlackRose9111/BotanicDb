
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("plant/<int:plant_id>", views.plant, name="plant"),
]

