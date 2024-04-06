from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.models import User, Group

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, throttle_classes

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


from .throttles import TenCallsPerMinute
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
        category = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)

        if category:
            items = items.filter(category__category_name=category)
        
        if to_price:
            items = items.filter(price__lte=to_price)
        
        if search:
            items = items.filter(title__icontains=search)
        
        if ordering:
            ordering_fields = ordering.split(',')
            items = items.order_by(*ordering_fields)
        
        paginator = Paginator(items, perpage)
        try:
            items = paginator.page(page)
        except EmptyPage:
            items = []

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

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response("This is secret message.")

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response('Throttle check anon')

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response('Throttle check user')

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_custom(request):
    return Response('Throttle check custom')


@api_view()
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        managers = Group.objects.get(name='Manager')
        user = get_object_or_404(User, username=username)
        if request.method == "POST":
            managers.user_set.add(user)
        elif request.method == "DELETE":
            managers.user_set.remove(user)

        return Response({"message": "ok"})


    return Response({"message": "error"}, status.HTTP_400_BAD_REQUEST)
