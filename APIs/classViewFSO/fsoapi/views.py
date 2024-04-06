from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .throttles import TenCallsPerMinute
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MenuItemViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    search_fields = ['title', 'category__title']
    #throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_permissions(self):
        permission_classes = []
        if self.action in {'create', 'list'}:
            permission_classes = [IsAuthenticated]
        
        return [perm() for perm in permission_classes]

    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        elif self.action == 'list':
            throttle_classes = [TenCallsPerMinute]
        else:
            throttle_classes = [AnonRateThrottle]
        return [throttle() for throttle in throttle_classes]