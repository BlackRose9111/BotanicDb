
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("plant/<int:plant_id>", views.plant, name="plant"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
]

