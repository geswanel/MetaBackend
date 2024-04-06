from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view(), name='menu'),
    path('menu-items-func', views.menu_items, name='menu-items'),
    path('menu-html', views.menuhtml, name='menu-html'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-id'),
    path('category/<int:pk>', views.category_detail, name='category-detail'),
    path('secret', views.secret),
    path('api-auth-token', obtain_auth_token),
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check_auth),
    path('throttle-check-custom', views.throttle_check_custom),
    path('groups/managers/users', views.managers) 
]