from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menu-items', views.MenuItemViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='menu-items'),
    path('menu-items/<int:pk>', views.MenuItemViewSet.as_view({
        'get': 'retrieve',
    }), name='menu-single-item'),
    path('api-auth-token', obtain_auth_token, name='auth-token')
]