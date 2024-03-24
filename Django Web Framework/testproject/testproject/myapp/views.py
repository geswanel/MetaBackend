from django.shortcuts import render
from django.views import View

from . import models

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import MenuItemForm, CategoryForm
from .models import Dish, Category

from django.contrib.auth.decorators import permission_required, user_passes_test

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dish_description(request, dish_id):
    dish = models.Dish.objects.get(pk=dish_id)
    return HttpResponse(f"Dish {dish}")

def menu(request):
    dishes = models.Dish.objects.all()
    return render(request, "menu.html", context={'items': dishes})

def httpdata(request):
    method = request.method
    path = request.path
    content = "<h1>Http Request arguments</h1>"\
        "<p>Method: {}</p>" \
        "<p>Path: {}</p>".format(method, path)

    return HttpResponse(content)

class MyView(View):
    def get(self, request):
        return HttpResponse("get from class based view")

@permission_required('myapp.add_dish')
def create_menu_item(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            category_name = form.cleaned_data["category"]
            Dish.objects.create(
                title=title,
                description=description,
                price=price,
                category=Category.objects.get(category_name=category_name)
            )

            return HttpResponseRedirect(reverse("myapp:index"))
    else:
        form = MenuItemForm()
    
    return render(request, "menuitemform.html", context={"form": form})

@user_passes_test(lambda user: user.is_authenticated and user.has_perm('myapp.can_create_category'))
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("myapp:index"))
    else:
        form = CategoryForm()
    return render(request, "categoryform.html", context={"form": form})