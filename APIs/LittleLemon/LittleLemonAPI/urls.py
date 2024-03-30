from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view(), name='menu'),
    path('menu-items-func', views.menu_items, name='menu-items'),
    path('menu-html', views.menuhtml, name='menu-html'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-id'),
    path('category/<int:pk>', views.category_detail, name='category-detail')
]