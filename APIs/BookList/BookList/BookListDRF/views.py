from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet


# Create your views here.
@api_view(['GET', 'POST'])
def books(request):
    return Response("List of books", status=status.HTTP_200_OK)


class ClassA:
    @staticmethod
    @api_view()
    def classMethodView(request):
        return Response("This is a class method view", status=status.HTTP_200_OK)


class ClassBasedView(APIView):
    def get(self, request):
        return Response("This is class based view", status=status.HTTP_200_OK)


class CRUDset(ViewSet):
    def list(self, request):
        return Response("Viewset list", status=status.HTTP_200_OK)

    def create(self, request):
        return Response("Viewest Create", status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        return Response("Viewest Create {pk}", status=status.HTTP_200_OK)
    
    def partial_update(self, request, pk=None):
        return Response(f"ViewSet partial update {pk}", status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response(f"Viewest destroy {pk}", status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        return Response(f"Viewest retrieve {pk}", status=status.HTTP_200_OK)
    
