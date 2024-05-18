# Description
Cheatsheet is a big chunk of monolite code with every snippet from the course.
Files divided using comments. 
For templates html is ommited.

# TODO
- [Admin notes](./README.md#admin)

## Cheatsheet
### CLI commands
- packages (django, mysqlclient, django_debug etc)
- Virtual environment using venv or pipenv
```bash
pip install pipenv
pipenv shell
pipenv install package

py -m pip install --upgrade pip

python -m venv path
./path/scripts/activate
pip3 install package
deactivate

django-admin startproject myproject .
python manage.py startapp myapp

python manage.py migrate
python manage.py makemigrations
python manage.py sqlmigrate
python manage.py showmigrations

python manage.py runserver

python manage.py shell


mysql -u root -p
show databases;
show tables from database;
use database;
```

### Django
```python
# settings.py
INSTALLED_APPS = [  # add app to installed
    ...,
    'myapp', # or myapp.myappConfig from app.py
]

DATABASE = {
    "default": {    # Add MySQL instead of SQLite
        "ENGINE": "django.db.backends.mysql",
        "NAME": "dbname",
        "HOST": "dbaddress",
        "PORT": "dbport",
        "USERNAME": "username",
        "PASSWORD": "password",
        "OPTIONS": {
        }
    },
    "mydb": {...} # config for several db
}

TEMPLATES = [
    {
        ...,
        "DIRS": [], # adding dirs to templates
        ...
    }
]

STATIC_URL = "static/"
STATIC_DIRS = [...]

# project/urls.py
from django.urls import path, include
from myapp import views

urlpatterns = [
    path("url/", include("myapp.urls")), # mapping urls from another app
    path("admin/", include("admin.urls")),  # admin - exist by default
    path("url", views.view, name="name"), # name for namespace + view from another app
]

handler404 = "myapp.views.view"

# app/urls.py
from django.urls import path, include
from . import views

app_name = "myapp" # for namespacing => reverse("myapp:func") or {% url "myapp:class" %}
urlpatterns = [
    path("url", views.myview, name="func"), # func based view
    path("url/<int:par>", views.MyView.as_view(), name="class"), # class based view + dynamic route with path parameters
    path(r'regex', ...) # why do we need regex urls?
]

# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
    FormView
)
from .models import MyModel

def myview(request):
    if request.method == "GET":
        try:
            items = MyModel.objects.get(pk = 1)
        except MyModel.DoesNotExist:
            raise Http404("mesage")

        return render(request, "mytemp.html", {"item": item})
    
    if request.method == "POST":
        field1 = request.POST.get("field1")
        ...
        MyModel.objects.create(field1=field1, ...)
        return HttpRedirect(...) # is redirect needed for post request? Corey

    return HttpResponse("Other http method")


class MyClass(View):
    def get(self, request):
        context = {"key": "value"}
        return render(request, "mytemp.html", context)  # rendering a template with dynamic data
    
    def post(self, request):
        instance = MyModel()
        # Create
        instance.save()
        MyModel.objects.create(field1=field1, ...)
        # Retrieve
        MyModel.objects.get(pk=1)
        MyModel.objects.filter(criteria) # name__startswith="H"
        MyModel.objects.all()
        # Update
        instance.field1 = value2
        instance.save()
        # Delete
        instance.delete()

        # Form api
        form = MyForm(request.POST)
        if form.is_valid():
            form.cleaned_data["name"] # to get value
        return HttpResponse("response")


class MyCreateView(CreateView):
    model = MyModel
    template_name = "template"  # what are default for generic views?

# models.py
from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    field1 = models.IntegerField(default=0, primary_key=True)
    field2 = models.CharField(max_length=255)
    field3 = models.DecimalField(max_digits=6, decimal_places=2)
    field4 = models.EmailField(max_length=255)
    field5 = models.URLField(max_length=255)
    # Other types of fields

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    OneToOne = models.OneToOneField(User, on_delete=models.PROTECT)
    ManyToMany = models.ManyToManyField(User, on_delete=models.RESTRICT)

    
    def __str__(self): # for django admin and shell to identify model instanse
        return field1
    
    class Meta:
        db_table = "table_name" # app_model by default

# admin.py
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from . import models
# Register your models here.
admin.site.register(models.MyModel)

admin.site.unregister(User)

@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True
        
        return form

# forms.py
from django import forms

class MyForm(forms.Form):
    field1 = forms.CharField(label=..., max_length=255, initial_text="")
    field2 = forms.IntegerField(required=True)
    field3 = DateField(widget=NumberInput(attrs={"type": "date"}))  # using widgets


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = "__all__" # or ["field1", "field2" etc]
```

### Templates
```html
<!-- 404.html -->
error message not found

<!-- base.html -->
{% load static %}
...
{% include 'header.html' %}
{% block content %}
{% endblock %}
{% include 'footer.html'}
...
<!-- mytemp.html -->
{% extends 'base.html' %}

{% block content %}
<h1>{{ title }}</h1>

{% for item in items %}
    <p>{{ item | upper}}</p> <!-- Filters: upper, lower, title, slice[start:finish], length, wordcount,  -->
{% endfor %}
<a href="{% url 'myapp:func' %}">link</a>
<img src="{% static 'static/url' %}">

<form action="{% url 'myapp:name' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }} <!-- form from generic view or passed manually as_div, as_table-->
    <input type="submit" value="OK">
</form>
{% endblock %}
```

- Info
    - **There are a lot of different DTL tags and filters**