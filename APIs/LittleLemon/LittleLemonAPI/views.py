from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from . import models, serializers


# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.HyperlinkedMenuItemSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = models.MenuItem.objects.select_related('category').all()
        items_serializer = serializers.MenuItemFuncSerializer(items, many=True)
        return Response(items_serializer.data)
    if request.method == 'POST':
        item_serializer = serializers.MenuItemFuncSerializer(data=request.data)
        item_serializer.is_valid(raise_exception=True)
        item_serializer.save()
        return Response(item_serializer.data, status=status.HTTP_201_CREATED)


@api_view()
@renderer_classes([TemplateHTMLRenderer])
def menuhtml(request):
    items = models.MenuItem.objects.select_related('category').all()
    item_serializer = serializers.MenuItemSerializer(items, many=True, context={'request': request})
    return Response({'data': item_serializer.data}, template_name='menutr.html')



@api_view()
def category_detail(request, pk):
    category = get_object_or_404(models.Category, pk=pk)
    category_serializer = serializers.CategorySerializer(category)
    return Response(category_serializer.data)


"""
{
    "title": "Pizza Margaritta",
    "price": "10.99",
    "inventory": 10
}
"""