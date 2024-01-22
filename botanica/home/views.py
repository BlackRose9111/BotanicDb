from django.shortcuts import render

# Create your views here.


async def index(request):
    return render(request, "home/index.html")
