from django.shortcuts import render

from . import models

from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, this is index page!")

def dish_description(request, dish_id):
    dish = models.Dish.objects.get(pk=dish_id)
    return HttpResponse(f"Dish {dish}")

def menu(request):
    dishes = models.Dish.objects.all()
    return render(request, "menu.html", context={'items': dishes})