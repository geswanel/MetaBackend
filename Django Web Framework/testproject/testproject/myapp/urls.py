from django.urls import path

from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:dish_id>/', views.dish_description, name="description"),
    path('menu/', views.menu, name='menu'),
    path('classbased/', views.MyView.as_view(), name='class_view'),
    path('httpdata', views.httpdata, name='httpdata')
]