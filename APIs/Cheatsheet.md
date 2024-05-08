# Description
Cheatsheet of DRF and questions to it!


## To Read
- REST
- SOLID


# Cheatsheet

## CLI
- packages `django` `djangorestframework` `djangorestframework-xml` `djangorestframework-yaml` `djangorestframework-csv` `djoser` `django-debug-toolbar` `djangorestframework-simplejwt~=version`
```bash
pip3 install pipenv

pipenv shell # create and run venv
pipenv install package

django-admin startproject prname .
python3 manage.py startapp api
python3 manage.py runserver

pip3 freeze > requirements.txt

```

## Settings
```python
INSTALLED_APPS = [
    #...
    'rest_framework',
    'rest_framework.authtoken', # adding token authentication
    'debug_toolbar',
    #...
]

INTERNAL_IPS = ['127.0.0.1']

MIDDLEWARE = [
    #...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #...
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework_yaml.renderers.YAMLRenderer",
        "rest_framework_csv.renderers.CSVRenderer",
        "rest_framework_xml.renderers.XMLRenderer",
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPaginator',
    'PAGE_SIZE': 2,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication', # set built-in token authentication    
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '10/second',
        'mythrottle': '5/day',
    }
}

```

## Models
```python
from django.db import models

class MyRelatedModel(models.Model):
    def __str__(self):
        return ""

class MyModel(models.Model):
    related = models.ForeignKey(MyRelatedModel, on_delete=models.CASCADE)
    pass
```


## Serializers
```python
from rest_framework import serializers

from .models import MyModel, MyRelatedModel

class MyRelatedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyRelatedModel
        fields = "__all__"

class MyModelSerializer(serializers.ModelSerializer):
    calculated = serializers.SerializerMethodField(method_name="mymethod")
    related = StringRelatedField()
    alias_field = serializers.CharField(source=model_field)
    class Meta:
        model = MyModel
        fields = "__all__"
    
    def my_method(self, obj):
        val = self.
        return val

class MyModelSerializer2(serializers.ModelSerializer):
    related = MyRelatedModelSerializer()
    class Meta:
        model = MyModel
        fields = "__all__"

class MyModelSerializer3(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = "__all__"
        depth = 1

class MyModelSerializer2(serializers.ModelSerializer):
    related = HyperlinkedRelatedField(queryset=MyRelatedModel.objects.all()) # search in docs
    # HyperlinkedModelSerializer
    class Meta:
        model = MyModel
        fields = "__all__"


class MySerializers(serializers.Serializer):
    field1 = serializers.CharField(max_length=200)
    #...
    def save(self):
        email = self.validated_data['email']
        #...

```

## Views
```python
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.views import generics, APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.core.pagination import Paginator
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


from .throttles import MyThrottle
from .serializers import MyModelSerializer
from .models import MyModel

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def func(request):
    items = MyModel.objects.all()
    
    myfield = request.query_params.get("myfield")
    perpage = request.query_params.get("perpage", default=2)
    if myfield:
        items.filter(myfield)
    

    paginator = Paginator(items, perpage)
    try:
        items = paginator.page(page)
    except EmptyPage:
        items = []
    
    serialized_items = MyModelSerializer(items, many=True)

    return Response(serialized_items.data, status=status.HTTP_200_OK)


class MyClassView:
    @staticmethod
    @api_view()
    def method_view(request, pk=None):
        item = MyModel.objects.get(pk=pk)
        serialized_item = MyModelSerializer(item)

        name = request.data.get('name')
        group = Groups.objects.get(name='groupname')
        group.user_set.add(User.objects.get(name=name))

        return Response(serialized_items.data, status=status.HTTP_200_OK)


class MyClassBasedView(APIView):
    throttle_classes = [MyThrottle]
    def get(self, request):
        
    def post(self, request):
        serialized_data = MyModelSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        title = serialized_data.validated_data['title']

        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class MyGenericView(generics.RetrieveUpdateAPIView):
    queryset = MyModel.objects.all()
    serializer = MyModelSerializer
    ordering_fields = [...]
    search_fields = [...]

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        if self.request.user.groups.filter(name='groupname').exists():
            permission_classes += [some permission] # how to do it for groups?
            
        return [permission() for permission in permission_classes]
    
    def get_throttles(self):
        throttles = [AnonRateThrottle]
        if self.request.user.is_authenticated():
            throttles = [UserRateThrottle]
        
        return throttles



class MyViewSet(viewsets.ViewSet):
    def list(self, request):
        pass
    
    def retrieve(self, request, pk=None):
        pass


class MyModelViewSet(viewsets.ModelViewSet):
    serializer = MyModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MyModel.objects.filter(user=self.request.user)

```

## Throttles
```python
from rest_framework.throttling import UserRateThrottle


class MyThrottle(UserRateThrottle):
    source = 'mythrottle'

```

## URL Conf
```python
# project
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatters = [
    path("", include("app.urls")),
    path("__debug__", include("debug_toolbar.urls")),
    path("api-auth-token", obtain_auth_token),      # set built-in token authentication
]

# app
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

# router example
router = DefaultRouter(trailing_slash=False)
router.register(r"123", views.MyViewSet)    # viewset without mapping each http method with viewset method

urlpatterns = [
    path("", views.my_view),
    path("1", views.MyView.as_view()),  # generics, class-based views
    path("", router.urls),
    path("viewset", MyOtherViewSet.as_view({    # viewsets
        "GET": "list",
        "POST": "create",
    }))
]


```