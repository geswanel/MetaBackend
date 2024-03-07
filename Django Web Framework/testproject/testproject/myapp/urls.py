from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:dish_id>/', views.dish_description, name="description"),
    path('menu/', views.menu, name='menu')
]