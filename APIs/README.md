



## 1 WEEK: REST APIs
### Course intro
- Introduction to the course
    - API - access to back-end
    - exchange info, access to functionality
    - pipenv packaging tool
    - REST API
        - Authentication and Authorization
        - Creating own api
    - DRF. Function and class based views for api
    - Serializers <-> Desirealize
    - Optimizing and protecting.
    - Little lemon restaurant api project
- Usage in real world - any app
    - **End to end fullstack development**
    - bank
    - End user and backend services
    - Designer Mocks -> Product designer -> API design. request-response structure
        - Who end user and other people => security, credentials, integrity
    - Components of large apis
### Introduction to API
- HTTP/HTTPS(encryption)
    - Client-server architecture
    - Request, Response cycle
        - Request: Version, path, method, headers, body
            - Headers examples: cookies, user-agents, refers
        - Response: Requested resource, content type, content length, headers
            - ETags, time last modified, http status code 
    - http methods methods
        - verbs
            - get - no payload
                - get or path parameters to filter APIs output
            - post (body = json or form url encoded data. payload)
            - put - update resource (same body as put + identificator of resource)
            - patch - update a part of resource
            - delete
        - helps REST APIs endpoint to identify what operation to perform (CRUD)
    - Status codes - sending appropriate status code with response
        - 100-199 - Informational (102 processing)
        - 200-299 - Success, 200 successful, 201 created
        - 300-399 - Redirect 301 - permanently moved (redirection from old endpoint (url))
        - 400-499 - Client side error. Bad request, No resources
            - 400(invalid payload), 401(unauthorized), 403(forbidden), 404(No resource)
        - 500-599 - Server side error, 500
        - Status code and its meaning depend on method
    - Response types
        - text/html
        - application/json
        - application/xml text/xml
        - texm/yaml application/x-yaml application/yaml
- RESTfulness
    - API - gateway to backend data
    - REST - architectual style for designing APIs
        - Easy way to send request and get responses with server
        - Constraints
            - Server-Client
            - Cacheable - responses can be saved to reduce load by reusing api result
            - Stateless - doens't have client state (who or previous requests) without propper user information
            - Layered - application can be divided into layers
                - FireWall
                - LoadBalancer
                - WebServer
                - Database
            - Uniform interface - unique interface, unified procedures
            - Optional code on demand
        - Resources
            - types examples
                - /orders api - Order object, list object, customer object, menu-item object
                - /menu-items api - menu items object, GET parameters
- Naming conventions - clear consice meaningful full words. endpoint = URI or url path
    - lowercase letters and hyphens between words
    - variables in camelCase between `{}` `orders/{orderId}/menu-items`
    - `/` used for hierarcy `orders/{orderId}/menu-items` `library/books/{bookId}/author`
    - Only use nouns. Plural for collection
        - avoid using method name in endpoint => these should be in HTTP request method
        - delete => `user/{userId}`
        - patch, put => `order/{orderId}`
    - Never use file extension => but how to let user choose what type of resource they want
        - as a query string parameter `order/{orderId}/?format=json`
        - minified or original version of a static file => `/assets/js/jquery/3.6.0/min` `/assets/js/moment/29.2.0/original/`
    - Filtering result using query string parameters.
        - `/menu-items/?category=main`
    - Never add a `/` at the end => `/orders/{orderId}`
    - Good routes vs bad routs
        - Multiple users should be separated by comma `/users/12,23,24/address
- Essential tools for API development
    - cmd and graphical tools
    - curl - http calls from a command line
        - `curl address` for get
        - `curl -d body address` for post body in (`@file` with json or query string parameters
         , `"param1=value1&param2=value2"` ,`"json inside"`)
    - postman - test and debug apis. GUI and web version
        - explore postman
    - **Insomnia** rest client - interface
        - store organize execute REST API requests
        - Creating request collection
            - creating http request. Choosing type of method and api url.
            - Post and get response. Form url or json
    - `httpbin.org` - website that helps to play with http methods
- Environment
    - VS code
    - python
    - vs code python extension
    - python indent + djaneiro extensions
    - pipenv - package manager => creating virtual environment so that you can manage your dependencies `pip3 install pipenv`
- [Creating Django project using pipenv](https://www.coursera.org/learn/apis/supplement/oQrdH/optional-creating-a-django-project-steps-and-code)
    1. `pipenv install django`
    2. `pipenv shell` to run virtual environment
    3. creating a project and an app and running a server. Running a server with different port
        - `django-admin startproject prname .` to create a project folder in the current (not a new folder)
    4. Configuring python interpreter in VS code
- Know your tools - Insomnia
    - filtering [] or ., creating requests

- [Additional Resources](https://www.coursera.org/learn/apis/supplement/D1h15/additional-resources)

### Principles of API development
- REST best practices
    - KISS - keep it simple stupid
        - one api - one specific job and do it well? bad example
            - choosing item of a day = 1 api with 2 calls - remove status OFF, put status ON
    - Filter, Order, Paginate - provide ability to do it
        - query string parameters
            - `?perpage=4&page=10`
    - Versioning - versioning of apps
        - maintain 2 version of any given resource
    - Caching - relevant => avoid heavy load
    - Rate limiting, monitoring
        - limits calls
        - monitor latency and status codes, network bandwith
- Security and authentication in REST api
    - Security
        - SSL = secure sockets layer - encryption - SSL certificate => `https://`
        - Signed URLs - calls only from your app and website only.
            - Limited access for a brief period of time
            - Signature of authentic source
                - `HMAC` signature => some secret key
        - Authentication
            - password-based => frustrating for every call
            - token-based over http-based authentication
                - after password-based authentication user receive token from the server
                - every api call will include a token as an http header
                    - matching with user
                    - adhoc policy or JWT (json web token)
            - Http codes. 401, 403
        - Cross-origin resource sharing CORS policy and firewalls
            - CORS - accepts calls from some specific domains
        - Firewall - only specific ip addresses
    - Web APIs risks because they are public (anyone can make calls with endpoint)
- Access control - little lemon - a lot of types of resources
    - Manager and delivery person
    - Access control - what users and what data
    - Roles (group) and priviliges (permission). Detailed and specific
        - Customer role (browse menu items, add, orders, reviews, own orders)
        - Manager (CRUD menu items, browse all orders, browse customer and transaction data, assign orders to the deliver)
        - Delivery (browse orders assigned to them, update status)
        - General manager
        - One user with multiple roles
    - Authorization = access control - authority after access
    - Authentication - access
    - Design and planning priviliges and roles
- Difference between authentication and authorization = security
    - Authentication - lets you in. pass user credentials to log in
        - Steps: Client passes theirs credentials => API web server identifies them and generate a token for the client => token is sent back to the client and is saved in **the cookies** => Every next api call is accompanied by this token to authorize a client!
        - 401 - unauthorized if there is no user with credentials
    - Authorization - lets you act. check roles and priviliges
        - after getting the api call with token => token verified => user priviliges checked => task performed
        - 403 - forbidden
        - extra layer
        - Example of creating priviliges = tasks that API user performs
            - Bookshop
                - Browse the books
                - Add new books
                - Edit books
                - Delete books
                - Place orders
            - This priviliges can be assigned to different roles
            - developer checks user group and than decides to deny or allow an action
    - Creating groups and assigning permissions in `django admin site`


### Writing your first API
- Book List API project
    - [creating pipenv project](https://www.coursera.org/learn/apis/supplement/oQrdH/optional-creating-a-django-project-steps-and-code)
        - updating pipfile with dependencies `django djangorestframework djangorestframework-xml djoser` => `pipenv install`
    - CRUD API project
    - Requirements:
        - Website and mobile app
        - Managers: Add and edit books quickly
        - Customers: Browse available books
    - Steps
        - Table in the database (Storage) => django models
            - `Title CharField(255), author CharField(255), price Decimal(5, 2), Inventory IntegerField`
        - API endpoints (2): 
            - `/api/books` - all the books list => out of stock filter
                - post request to create a new book
                    - Insomnia: 201 (created), 400 BadRequest (requirement data missing)
            - `/api/books/{bookId}` - only a particular book 404 if needed, or 200 not in a list
                - put
                - delete
                - url pattern `/api/books/<int:pk>
        - Serializing (model to json)
            - `django.forms.models.model_to_dict` `django.http JsonResponse(model_to_dict(model))`
        - payload
            - Json string `QueryDict(request.body)` class to parse json to a python dictionary
                - `.get` to access
- Organizing API with multiple apps
    - create app for different groups
        - particular set of relevant problems
    - Planning, Smaller aims, Multiple apps
        - Monolitic => too hard to maintain
    - Avoid global environment => always use virtual environment
    - Upgrades might break apps - create a new app for an update
        - Use versioning, keep old api intact, timely launch
        - Existed app, updated app
    - List your dependencies `requirements.txt` file
        - `pip3 freeze > requirements.txt`
        - `pipenv` PipLock (record dependencies)
    - Separate resource folders for each of your apps
        - Avoid conflixts, manage files
        - `+` app specific static files inside the app as templates
        - settings file for separate files to include in main settings
            - `Django split settings`
    - Place business logic into models. manage and organize code in one place
        - powerful, decoupled, reusable
    - [Consequences](https://www.coursera.org/learn/apis/supplement/KqDmX/consequences-of-a-poorly-designed-api-project)
        - Data breach => SSL and security
        - Data corruption => Solid authorization check + sanitizing and validating data before processing
        - Wastage of computer power and memory => Optimizations and database-related code validation, caching
        - Wastage of bandwith => Caching, Filtering, Pagination. Proper caching headers
        - Bad user experience => proper naming convention, **Accept header**, filtering, sorting, searching and pagination, proper error checking in the code to avoid 5XX
        - Breaking client application => update and current version
        - Failure to manage the app => Distribute the features to multiple apps, some business logic in the model
- XML and JSON response types. **Accept header**
    - JSON `Accept: application/json`. Javascript object notation
        - Simple, lightweigh
        - keys:values
        - easire to generate and pass
    - XML `Accept: application/xml or text/xml`. Extensible markup language
        - Readable, supports data attributes
        - tag based
        - has comments
    - Data conversion. DRF JSON renderer or third party for XML and YAML
- Debugging your API VS code
    - Watch and Breakpoints
    - Django debugger
- Browsers tools and extensions for API development
    - fetch("address") in console to initiate get call
    - Headers and data in network window
    - initiator - where was initiated
    - Disable cache checkbox
    - Clearing
    - **JSON formatter** extension for a browser (there is one in firefox)
- Mock APIs
    - API with fake data => so client side developers can start create their api without waiting while API finished
    - hardcoded responses
    - mock api endpoints, real endpoints
    - Steps: create mock data -> creating mock API endpoints
    - Tools
        - **Mock API data generator** browser tool `www.mockaroo.com`
        - **Mock API endpoints** `https://mockapi.io/`

### Module Summary


## 2 WEEK: Django REST framework\
### Intro to DRF
- DRF - toolkit on top of a django => help to build robust api quickly
    - Bridges regular django app with ORM and django
    - JSON, XML
    - **Serialization** - biggest benefit of DRF
        - easy to transform models to RESTful API
        - utility classes
        - models -> python data types -> json/xml/others
        - deserialization. request -> model + validation
    - Integration easy
    - Web browsable API - like Insomnia but worse
    - Own request response objects for more flexibility
    - Status module - human readable `Status.HTTP_200_OK`
    - CRUD helpers (get, post, patch, put, delete)
    - Authentication systems supported
    - External provider like facebook
- Installing and configuring DRF
    - pip - creating venv and managing everything by yourself
    - pipenv - easier
        - `pipenv install django`
        - `pipenv shell` activate env
            - starting project
            - starting app
            - `pip3 install djangorestframework` `pipenv install djangorestframework`
            - `INSTALLED_APPS.append('rest_framework')`
        - Writing a code. Response, Decorators, URLConf. Insomnia. Instructing about methods in api_view decorator `@api_view(['POST'])`
            ```python
            from rest_framework.response import Response
            from rest_framework import status
            from rest_framework.decorators import api_view

            @api_view()
            def books(request):
                return Response('List of books', status=status.HTTP_200_OK)
            ```
- Better API view with decorators ***api_view***
    - `@api_view()` decorator create interface for testing apis
    - passing method names. Post calls in interface in browser
    - Options - helpful information about the endpoint
    - Throttling and rate limiting
    - authentication
- Different types of Routing and url mapping in project. **Response everywhere**
    - Regular - `urls.py` `path` + `@api_view` decorator
    - class method - `@staticmethod` `@api_view` `path(endpoint, views.class.func)`
        - subclass of `object`!!!! (not from View)
    - class based view - subclass of `APIView` `as_view()` for urls + verbs for methods (get, post etc)
    - viewsets - `ViewSet` `list, create, update, partial_update, destroy, retrieve`
        - `as_view({method: func})` to map method to fun
    - `SimpleRouter(trailing_slash=False)` class - to work with viewsets `router.urls`, `router.register(endpoint, viewsetsubclass, basename)`
    - `DefaultRouter(trailing_slash=False)` class - same as simple router but gives list of endpoints in the root
- Generic views and ViewSets in DRF
    - Viewsets
        - `ViewSet` extends `APIView`
            - `list`, `create` methods
            - `retrieve` `update` `partial_update` `destroy` methods
            - From ViewSet you have to manually implement all functions
        - ModelViewSet - give `queryset` and `serializer` => handles CRUD automatically
        - ReadOnlyModelViewItem - Handles only get requests
    - Generic Views - require `queryset` and `serializer` to work properly
        - Classes
            - `ListAPIView`, `CreateAPIView`
                - `ListCreateAPIView`
            - `RetrieveAPIView` `UpdateApiView` `DestroyApiView`
                - `RetrieveUpdateAPIView`, `RetrieveDestroyAPIView`, `RetrieveUpdateDestroyAPIView`
        - Permissions and authentication
            - `permission_classes` public attribute in the class `permission_classes = [isAuthenticated]`
            - Selectively enable authentication for particular calls => override `get_permission` method
```python
def get_permissions(self):
    permission_classes = []
    if self.request.method != 'GET':
        permission_classes = [IsAuthenticated]
        
    return [permission() for permission in permission_classes]
```
            - example to retrieve orders for a authenticated user
```python
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Order.objects.all().filter(user=self.request.user)
```
        - It's possible to override default behaviour of http methods of generic class
- Function and class-based views
    - Function based views: easier to implement, use decorators, quickly write ones-off solution, better readability
    - Class based views: less code duplication, less code overall, inheritance, class method for every http method
        - passing GET parameters as query string `request.GET.get('')`
        - passing and getting form parameters or json `request.data.get('')
        - Creating class based view with get post methods
- Django debug toolbar
    - Installing
        - `pipenv install django-debug-toolbar`
        - `settings.INSTALLED_APPS += ["debug_toolbar"]` `settings.INTERNAL_IPS = ['127.0.0.1']`
        - `settings.MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]`
        - `urls.urlpatterns += [path('__debug__'), include("debug_toolbar.urls")]`
    - Tools
        - SQL - optimization
        - Profiling - delays between requests and responses
        - Headers
        - Caching
- Restaurant menu API project with DRF
    - Steps for CRUD project
        - create model and serializer
            - `app.serializers.py` `rest_framework.serializers.ModelSerializer` -> `Meta` -> `model, fields`
        - create views using generic views `ListCreateAPIView` `RetrieveUpdateDestroyAPIView`
            - `queryset = model.objects.all` `serializer_class = Class`
        - ULRConf this views
        - Naming conventions (no trailing slash)
- [Additional Resources](https://www.coursera.org/learn/apis/supplement/SOhsP/additional-resources)

### DRF essentials
- method view
- Serializers = Conversion tool
    - Benefits
        - Check integrity and prevents data corruption
        - helps to convert to readable format
        - helps parsing json to model and model to json
        - validate information
    - Practical 
        - `serializers.py` app level file with serializers
        - queryset automatically converted by using `queryset.values()`
        - `serializers.Serializer` class used to create custom serializers
            - serializers fields => what fields will be presented => filtering fields to send
            - `many` argument
        - get object or 404
        - `serializer = Serializer(items, many=True/False)` => `Response(serializer.data)`
    - Problem with urls that I encountered! ('books' 'menu')
- Model serializers
    - subclass of `serializers.ModelSerializer`
        - nested `Meta` class with `fields`, `model`
            - fields name can be change (source argument of new field)
    - `SerializerMethodField` to calculate and retrieve a new field `method_name`
    - Decimal to work with number fields
    - Same usage
- Relationship serializers - A way to serialize foreign key of a table
    - example Category for menu-items `on_delete PROTECT`
    - Ways
        - Just pass to `fields` => ids for foreign keys
        - `RelatedField` type, `StringRelatedField`
            - `__str__` for representation
            - In view => select_related('').all() - load related model in a single sql call
    - Creating category serializer => using category serializer instead of `RelatedField` related field serialized to json
- Other types of serializers
    - Nested Fields
        - 2 ways to serialize nested
            - create category serializer and include to menu-item serializer
            - specifiing `depth=1` for MenuItem serializer => all fields of foreign keys
    - Hyperlinks
        - `HyperlinkedRelatedField` - queryset + view_name (if not match convensions)
            - Create a view for a related field and map it with conventions.
            - add `HyperlinkedRelatedField` to menuitem serializer and pass parameters
            - pass request to context when createing MenuItem serializer
                - `serialized_item = MenuItemSerializer(items, many=True, context={'request': request})` or differently to class views
        - `HyperlinkedModelSerializer` 
            - Model with related field shoudl extend from `HyperlinkedModelSerializer` => url patterns should match conventions
- Deserialization and validation
    - `Serializer(data=request.data)` => `serializer.is_valid(raise_exception=True)`
    - `serializer.save()` `serializer.validated_data`
    - return `Response(serializer.data, http201)`
    - requirements of related fields
        - `read_only=True` for realted field
    - category_id for posting id
        - `write_only=True`
    - it's possible to create multiple serializer for different call methods
- Renderers - display the api output in different formats
    - Renderers
        - Built-in
            - JSONRenderer
            - BrowsableAPIRenderer => Browsable API view (DRF browser view)
        - Third-party
            - XMLRenderer
            - JSONP Renderer
            - YAML Renderer
    - Using renderers
        - Header: Accept: `(application/json text/html application/xml)`
            - DRF response according to Accept header in request
        - `settings.REST_FRAMEWORK` setting variable to establish renderers
            ```python
            DEFAULT_RENDERER_CLASSES = [
                "rest_framework.renderers.JSONRenderer",
                "rest_framework.renderers.BrowsableAPIRenderer",
                "third party"
            ]
            ```
        - Installing `pipenv install djangorestframework-xml` to render xml
            adding to `REST_FRAMEWORK.DEFAULT_RENDERER_CLASSES` `rest_framework_xml.renderers.XMLRenderer`
        - `format query string parameter`
- Different types of renderers
    - TemplateHTMLRenderer => with using DTL
        - import `rest_framework.renderers.TemplateHTMLRenderer` `rest_framework.decorators.renderer_classes`
        - Create a view with decorators and return `Response(context, template_name='name')`
            - url mapping
        - Create template for it `myapp/templates/template.html`
    - `StaticHTMLRenderer` => without using DTL
        - Same import and creating view with decorators
    - CSV renderer `pipenv install djangorestframework-csv` => `text/csv`
        - `rest_framework_csv.renderers.CSVRenderer` same import and view with decorators
    - YAML renderer `pipenv install djangorestframework-yaml` => `application/yaml`
        - `rest_framework_yaml.renderers.YAMLRenderer` same import and view with decorators
    - Instead of importing CSV and YAML classes to view `renderer_classes`
        - Add them to `REST_FRAMEWORK.DEFAULT_RENDERER_CLASSES`
- TIPS - naming of ulrmapping using dash `category-detail` - convention - a lot of automatic work
- Questions
    - How to make read_only for post requests for different types of fields

### Module Summary

- [Additional Resources](https://www.coursera.org/learn/apis/supplement/tsdUA/additional-resources)


## 3 WEEK: Advanced API development
### Filtering ordering searching
- Filtering and Searching
    - 2 ways to handle it
        - Client side: Client gets all instances and filter it => long processing
        - Server side: Client passes parameters and server filters instances on it's side
    - Query string parameters `?par1=val1&par2=val2`
        - `request.query_params.get('')`
        - `if queryparam` => filtering or searching
    - Filtering and searching - **LOOKUPS**
        - `queryset.filter()` function
            - field lookups => `field__lookup`
                - `filter(price__lte=to_price)` - for usual fields
                - `filter(category__title=category)` - model__field for related fields
            - `search` param
                - `filter(title__contains)` `startswith` `icontains`
- Ordering
    - `django filter` package to use with class based views
    - Function based => django native `?ordering=price,inventory`
        - `queryset.order_by(field1, field2)` `-field => DESC`
        - splitting comma and unpacking `order_by(*ordering)`
- Data Validation - check if data is correct
    - Data requirements
    - methods
        - In the field `serializers.DecimalField(min_value=2)`
        - Using `extra_kwargs` in `Meta` class
        ```python
        class Meta:
            ...
            extra_kwargs = {
                "price": {'min_value': 2},
                "stock": {'source': inventory, 'min_value': 0}  # will add field without creating outside the Meta!
            }
        ```
        - `valid_field` methods => `ValidationError`
        ```python
        def validate_price(self, value):
            if value < 2:
                raise serializers.ValidationError("some text")
        ```
        - `validate` methods => all fields in one function
        ```python
        def validate(self, attr):
            if attrs['price'] < 2:
                raise serializers.ValidationError('sometext')
            
            return super.validate(attrs)

        ```
    - Unique validation `rest_framework.validators`
        - UniqueValidator
            - In the field `title = serializers.CharField(..., validators=[UniqueValidator(queryset=MenuItem.objects.all())])
            - In `extra_kwargs` in Meta
            ```python
            extra_kwargs = [
                'title': {
                    'validators': [UniqueValidator(queryset=MenuItem.objects.all())]
                }
            ]
            ```
        - `UniqueTogetherValidator`
            - in Meta
            ```python
            validators = [UniqueTogetherValidator(queryset, fields=['title', 'price'])]
            ```
- Data sanitization - clearing data from threats
    - HTML injection (JS malicious code injected and can be executed)
        - bleach third-party package `pipenv install bleach` in serializers
        ```python
        import bleach

        ...
            def validate_field(self, value):
                return bleach.clean(value)
            
            def validate(self, attr):
                attrs['title'] = bleach.clean(attrs['title'])
        ```
    - SQL injection => avoid using raw sql queries if it's possible
        - Do not use string formatting or quotations
    ``` python
    MenuItem.objects.raw("SELECT .... %s", [limit]);    #OK
    MenuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s' % limit) # not ok
    MenuItem.objects.raw("SELECT * FROM LittleLemonAPI_menuitem LIMIT '%s' ", [limit]) # not ok
    ```
- Pagination - sending results in smaller chunks
    - `perpage` and `page` get query string parameters
    - limit for perpage (10) => several calls (20) or bad request (50)
    - `django.core.paginator` moduel `Paginator` class and `EmptyPage` exception
    ```python
    def menu_items(self, request):
        ...
        perpage = request.query_params.get('perpage')
        page = request.query_params.get('page')

        paginator = Paginator(items, perpage=perpage)

        try:
            items = paginator.page(page)
        except EmptyPage:
            items = []
        #serializers
        #Response
    ```
- Deeper about pagination and filtering
    - Scaffolding a project with class based view based on `ModelViewSet`
    - creating url patterns for `list` and `retrieve` methods for get calls
        - `Class.as_view({'httpmethod': classmethod})
    - `REST_FRAMEWORK` setting
        - `DEFAULT_FILTER_BACKENDS`
            - `django_filters.rest_framework.DjangoFilterBackend`
            - `rest_framework.filters.OrderingFilter`
            - `rest_framework.filters.SearchFilter`
        - `DEFAULT_PAGINATION_CLASS: rest_framework.pagination.PageNumberPaginator`
        - `PAGE_SIZE`
    - Viewset class
        - `ordering_fields=[]`
        - `search_fields=[]` `related__field` for related fields
- Caching - Saving results
    - Can happen in multiple layers
        - Client
            - Caching headers => cache for a specific time
        - Reverse proxy - distribution of requsts
            - Caching headers => cached result for a specific time
        - Webserver
            - check if nothing changes
            - simple files, a database, catching tools (redis)
                - database cache to avoid connections
        - DB server
            - query cache: sql query, query results
            - Connections still happening => disadvantage

- [Additionl Resources](https://www.coursera.org/learn/apis/supplement/rw4od/additional-resources)

### Securing an API in DRF
- Token-based authentication in DRF
    - Password based for first call
    - Token based for next - long, hard to read, expires, 
        - validation and matching
        - `TokenAuthentication` class
        - Steps
            - settings `rest_framework.authtoken` to installed apps
            - migrate
            - create superuser and create token in admin panel
            - create function view
                - `rest_framework.permissions IsAuthenticated`
                - `rest_framework.decorators permission_classes`
            - `DEFAULT_AUTHENTICATION_CLASSES += ['rest_framework.authentication.TokenAuthentication']`
            - Insomnia: Bearer token: Token prefix + token generated in admin panel
        - Generating token by password authentication
            - `rest_framework.authtoken.views.obtain_auth_token`
                - Takes post request for authentication and generate token that can be used in next calls.
- User roles => authorization = priviliges checking
    - Creating roles (groups) and users, assigning roles to a user
    - if else blocks inside the view
        - `request.user.groups.filter(name='groupname').exists()` condition
- Setting up API throttling (rate limiting)
    - Base classes
        - Anonymous throttling - `rest_framework.throttling.AnonRateThrottle`
        - User throttling (don't forget permissions) - `...UserRateThrottle`
    - throttles.py for custom throttles
    - `DEFAULT_THROTTLE_RATES` setting for `REST_FRAMEWORK`
        - `anon='2/minute'` `user='5/minute'` `'custom'='10/minute`
    - Function based views
        - `rest_framework.decorators.throttle_classes`
            - Anon, User
            - Custom - Subclass of Anon or User with `scope` member variable for throttling name for using in settings
    - Class based views - project scaffolding
        - Creating ModelViewSet for menu items and mapping urls for it
        - adding `DEFAULT_THROTTLE_CLASSES` to `REST_FRAMEWORK` in the settings
        - Getting throttle classes in class
            - using `throttle_classes` member variable
            - using `get_throttles(self)` function to conditionally define throttles. Exclude throttle_classes variable
                - f.e. for post method `self.action == create`
    - Standard rates
        - Messengers api 100-80/second, Facebook Instagram API 200/hour
- Intro to Djoser library for better authentication
    - install `pipenv install djoser`
    - configuration: Installed app (under rest_framework)
        - `DJOSER` setting variable `USER_ID_FIELD: "username"` (LOGIN_FIELD: EMAIL) pk for user model
        - Adding `SessionAuthentication` to be able to use browsable api view
        - `path('auth/', include(djoser.urls))`
        - `path('auth/', include(djoser.urls.authtoken))`
        - migrate
    - List of used endpoints in djoser
        - /users/ - all users (get) + creation(post)
            - me/ - with token => details of user (get) + update email(put)
            - confirm/
            - resend_activation/
            - set_password/
            - reset_password/
            - reset_password_confirm/
            - set_username/
            - reset_username/
            - reset_username_confirm/
        - /token/
            - login/ - generate token
            - logout/
    - Login as superuser to use browsable api with djoser
    - supports JWT - json web token for authentication. 2 tokens access and refresh
        - installing `pipenv install djangorestframework-simplejwt~=5.2.1`
        - configuration
            - installed apps => `rest_framework_simplejwt`
            - REST_FRAMEWORK.DEFAULT_AUTHENTICATION_CLASSES
                - `rest_framework_simplejwt.authentication.JWTauthentication`
            - adding patterns to `rest_framework_simplejwt` `TokenObtainPairView`, `TokenRefreshView` f.e. `api/token/` and `api/token/refresh/`
            - Establish expiration of access token `SIMPLE_JWT = {ACCESS_TOKEN_LIFETIME = timedelta(minutes=5)}`
            - blacklist app configuration (`TokenBlacklistView` view) (`token_blacklist` app of simple_jwt)
            - `migrate`
        - generate token `api/token/` with user credentials => 2 token returns
        - Regenerate token `api/token/refresh/` = form parameter `refresh = refresh_token`
        - blacklist token `api/token/blacklist/` same form parameter
- User account manager
    - user registration endpoints
        - Djoser - `auth/users/`
            - credentials can be passed using a post call to create a new user. No token needed.
            - Admin user can see all users but not admin only themselves.
    - superuser endpoints
        - Permission `IsAdminUser`
        - Create endpoint to assign users to manager group by username
            - Create manager group in admin
            - use User and Group models `django.contrib.auth.models`
            - request.data - parsed data from request body
            - get user and get group
            - `managers.user_set.add(user)`

- [Additional Resources](https://www.coursera.org/learn/apis/supplement/qfFJn/additional-resources)

## 4 WEEK: Recap and Project

- Final assessment
    - LittleLemon api project. Peer Review
    - Final quiz
- Project introduction video
    - 3 types of users
        - Managers
        - Managers
            - add edit and remove menu items `/api/menu-items/`
            - add a user to a delivery group `/api/users/{userId}/groups`
            - browse orders `/api/orders` - filter by status delivered or pending
            - assign to a delivery person `/api/orders/{orderId}`
        - Customers
            - Browse menu-items. filter by categories and price ranges, search menu-items
                - add to cart - /api/users/{userId}/cart/menu-items
                - place an order - /api/order => emptied cart
                - flush cart - /api/users/{userId}/cart
                - one cart with multiple items
                - can view own orders, status and total price
        - Delivery
            - Browser orders assigned to them api/orders/{orderId} /api/orders
    - Registration and authentication `/api/users`
    - api endpoints to assign users to a group `/api/users/{userId}/groups`
    - Token for endpoint
    - Throttling (5 api calls per minute)
    - Tools
        - vs code
        - django and drf
        - virtual environment
        - insomnia
        - only token-based authentication
- Project structure and API routes
    - Structure 
        - One app LittleLemonAPI with all endpoints in it
        - use pipenv to manage dependencies
    - Function or class based views can be used
        - follow api naming conventions
    - User groups - Create some users to both groups. No group -> customer
        - Manager
        - Delivery crew
    - Error check and proper status codes
        - 200 - success other requests (get, put, patch, delete)
        - 201 - success post requests
        - 403 - no permission (failed authorization)
        - 401 - not authenticted
        - 400 - validation failed
        - 404 - non-existing resource
    - Endpoints
        - registration, token generation
            - `/api/users` - no role; POST; creating new user (name, email, password)
            - `/api/users` `users/me` - valid token; GET; displays only current user
            - `/token/login` - valid username and password; POST; generate token
                - djoser?
        - Menu items endpoints
            - `/api/menu-items`
                - GET - list all menu items
                - POST, PATCH, PUT, DELETE
                    - Customer, Delivery crew (403 unauthorized)
                    - Manager (Creates a new item and returns 201)
            - `/api/menu-items/{menuItem}`
                - GET - single menu item
                - Customer, Delivery crew - unauthorized for POST, PUT, PATCH, DELETE
                - Manager
                    - Put, Patch - updates a single menu item
                    - delete - deletes it
        - User group management endpoints - only for **Managers**
            - `/api/groups/manager/users`
                - GET - all managers
                - POST - assigned the user in the payload to managers (201)
            - `/api/groups/manager/users/{userId}`
                - DELETE - removes user from managers user (200) or if not found (404)
            - `/api/groups/delivery-crew/users`
                - GET - all delivery crew
                - POST - assign the user to delivery crew (201)
            - `/api/groups/delivery-crew/users/{userId}`
                - DELETE - removes from delivery-crew (200) or (404) if not found
        - Cart management endpoints - for customer
            - `/api/cart/menu-items`
                - GET - list of cart items
                - POST - add item to cart. set user id to the cart items
                - DELETE - delete all menu items
        - Order management endpoints
            - `/api/orders`
                - GET
                    - **Customer** - all orders with items created by this user
                    - **Manager** - all orders for all users
                    - **Delivery crew** - assigned orders
                - POST - **Customer** creating a new order. getting items from cart and transfering to order-items, flush cart
            - `/api/orders/{orderId}`
                - GET
                    - **Customer** - all items for this order id for this user (not user's order - error status code)
                - PUT, PATCH
                    - **Manager** - update status (0 - out for delivery if crew assigned, 1 - delivered) and delivery crew
                - DELETE
                    - **Manager** - deletes order
                - PATCH
                    - **Delivery Crew** - update order status
    - Additional steps
        - implementing filtering, ordering, pagination to menu-items and order endpoints
    - Throttling