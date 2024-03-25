from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name="book-list"),
    path('books/<int:pk>', views.BookItem.as_view(), name="book-item"),
]
