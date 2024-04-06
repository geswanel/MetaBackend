from django.urls import path
from . import views

# Instead of as_view(dict) for Viewsets
# r = SimpleRouter(trailing_slash=False) or DefaultRouter
# r.register(endpoint, ViewSetClass)

# urls = [path(endpoint, view)] + r.urls
# or
# urls = [
#     path(...),
#     path(endpoint, include(r.urls))
# ]

urlpatterns = [
    path('book-items', views.books, name='book-list'),
    path('book-items/<int:pk>', views.book_detail, name='book-detail')
    # path('books/', views.books, name="book-list"),
    # #path('books/<int:pk>', views.BookItem.as_view(), name="book-item"),
    # path('classmethod/', views.ClassA.classMethodView, name="class-method"),
    # path('classbasedview/', views.ClassBasedView.as_view(), name="class-based"),
    # path('viewset/', views.CRUDset.as_view({
    #     "get": "list",
    #     "post": "create"
    # }), name='viewset-all'),
    # path('viewset/<int:pk>', views.CRUDset.as_view({
    #     "get": "retrieve",
    #     "put": "update",
    #     "patch": "partial_update",
    #     "delete": "destroy"
    # }), name="viewset-id")
]
