


## 1 WEEK: introduction to Django

### Intro
- Introduction to the course
    - Django => url => MVT
        - Views
        - Models
        - Templates
- What is Django? - Web framework - a toolking to create webapplications without reinventing the wheel
    - Usage
        - ML and AI
        - SaaS
        - Scalable Web Applications
    - Benefits
        - APIs, Libraries, Templates
        - Documentation, Community
        - Fault Tolerance, Scalability, secure, 
        - DRF - back-end service
        - Open Source
        - high volumes of content
- How django is used in real world?
    - HTTP - data request and response
    - Flask? Light weight, no db management
    - FullStack exposure
- Installation
    - Python Installation
    - VSCode installatio
    - SQLite extension VScode
- Creating virtual environment and installing django
```bash
py -m pip install --upgrade pip

python -m venv path
./path/scripts/activate
pip3 install django
code .
deactivate
```
- [Labs tutorial](https://www.coursera.org/learn/django-web-framework/supplement/b35Pn/working-with-labs-in-this-course)
- [Additional resources](https://www.coursera.org/learn/django-web-framework/supplement/yqDlw/additional-resources)

### Project and Apps
- Static website structure - HTML(content), CSS(styles), JS(client side functionality)
    - `css, js, img` folders
- Dynamic web application: Internet Protocols <=> WebServer <=> Databases
    - HTTP protocol to communicate with webserver and DB to store data
    - Django comes with python written web server
    - Web framework provide infrustructure for this
- Django Project structure
    - Project - entire web application project
    - App - a submodule of a project that implements one functionality
        - App should be registered in project settings
        - Include: Models, Views, Templates, Templates Tags, Static, MiddleWare, URLs
    - django-admin and manage.py needed to perform administrative tasks
        - `python manage.py command`
            - `startapp`
            - `makemigrations` - migration - creation of db tables (every changes to tables)
            - `migrate`
            - `runserver` - run server at localhost
            - `shell` - some quick operations
    - project folder
        - `__init__.py` - declaring that it's a package
        - `settings.py` - configurations of application
            - `INSTALLED_APPS` - list of string with paths to apps. New apps should be added here
            - `DATABASES` - dict with db configurations. By default SQLite is used. Other db can be connected
            - `DEBUG = True` - debug mode - updates without restarting. Turn off at production
            - `ALLOWED_HOSTS` - list of strings where the site can be served. F.e. `0.0.0.0:8000` for externaly visible locally
            - `ROOT_URLCONF` - url patterns path of django project
            - `STATIC_URL` - path to folder with static files: JS, CSS, Images
        - `urls.py` - urlpatterns to match mapped view
        - `asgi.py` `wsgi.py` - web application servers of asgi and wsgi standards
```shell
django-admin startproject name path
python manage.py startapp appname
```
- Creating first project
    - virtual environment - isolate dependencies
    - Create project dir -> create virenv -> create django project -> run django project
    - activate and deactivate venv
```shell
mkdir project
cd project
python -m venv tutorial-venv
.\tutorial-venv\Scripts\activate
pip3 install django
python -m django version
django-admin startproject chefsList
cd chefsList
python manage.py runserver
```

### Admin and structures
- django-admin, manage.py commands
    - setup environment
    - `runserver` - ip and port can be specified
    - `startproject name dir`
    - manage.py local version of django-admin with project settings
        - automatically created with project
    - manage.py used for single project
        - django-admin can be used for multiple by switching settings
    - development server details
        - avoid using in production
- App structures
    - App - a piece of code to solve one problem
        - `python manage.py startapp demo` - creating app
            - urls - by default isn't created in app dir. => create it and add url pattern connected to view
                - include - connecting url pattern to another file with patterns
                - path - creating url pattern
                - URL conf
            - views - functions that called by django after parsing an url of client request
                - returns http response
                - Uses HttpRequest
                - should be mapped to url
            - models - database functionality
            - tests - adding tests
            - forms, serializers
    - App should be added in `settings.py` `INSTALLED_APPS`
```Python
# ulrs.py in project folder
urlpatterns = [
    path('/', include('demo.urls')),
    ...
]

# urls.py in app folder
urlpatterns = [
    path('', views.index, name='index')
]

# views.py in app folder
def index(request):
    return HttpResponse("Hello, this is the index page")
```

### Web Frameworks and MVT
- Web framework - structure and foundation to write code faster.
    - Static website can consist of HTML CSS JS but if some functionality needed?
        - Webapplication divided into front-end and back-end
        - front-end - React - user interface
        - back-end - data storage and retrieval and processing requests
    - Django - Fast, Secure, Reusable, feature-reach, scalable
    - Three-Tier architecture
        - Presentation level - user interface to communicate with web application
        - Application level - Ties presentation and data tier
        - Data level - database server to store and retrieve information
- MVT
    - MVC architecture
        - Controller handles requests and responses and communicate with Views and Models
        - Model is responsible for data definition, processing and interacting with db
        - View is a presentation layer - formats of response and sends to controler
    - MVT architecture
        - URL dispatcher - controller layer
            - Matches client url with url pattern and routes the flow to associated view
        - View - processing logic
            - Takes data from client request and communicate with DB using models to perform CRUD in order to response
            - a user-defined functions or a class
            - created inside an app
        - Model - data layer
            - a model is a class that is migrated by django into matching sql tables
            - ORM (object relation mapper) helps to perform CRUD in object-oriented way instead of invoking SQL queries
        - Template - presentation layer. Placed in `templates` folder inside app
            - Web page contains HTML and Django Template Language code blocks
            - Django Template Processor uses any context data from the view to create a dynamic response
            - view returns a response 
- MVT example
    - Usage of views to create HttpResponse with hello world
    - Usage of views to get data from model and HttpResponse
    - Usage of views to get data from model and render the template with data.

- Using `pip freeze` to create `requirements.txt` file with packages needed.

### Module summary
- Course intro
    - Why using Django? Fast, High 
- Project and Apps
    - create and identify basic project and apps
    - DRY - reusability
- Admin and Structures
    - django-admin and manage.py
    - Project and apps
- Web Frameworks
    - Fast development, Clean structure, Reusability
    - Three-tier architecture MVC
        - Django MVT
- [Additional Resources](https://www.coursera.org/learn/django-web-framework/supplement/0AF6Z/additional-resources)


## 2 WEEK: Views
### Views
- Views - a function or a class that process httprequest by processing, manipulating and retrieving data from DB and returning http response.
    - stored in `views.py` file in the app folder
    - Should be mapped to url (**routing**) so when user makes a request to url, needed view function is called
        - create a `urls.py` file in app folder
        - add `urlpatterns` list with urls using `path(url, view)` function
    ```python
    # views.py
    from django.http import HttpResponse

    def home(request):
        return HttpResponse("hello world")

    # ulrs.py
    from django.urls import path
    from . import views

    urlpatterns = [
        path("", views.home)
    ]
    ```
- Creating a view and Mapping urls
    - creating a base view with HttpRequest and mapping it to `urls.py` at app level
    - use `include` function in `urls.py` project level to include urlpatterns from app level
- View logic
    - Django url dispatcher invokes a corrseponding view function that matches the url pattern
    - View interacts with model and template
        - model interaction
            - retrieving all or certain object from DB or delete a row in DB (`GET`)
            - insert or update new object to db using request parameters (`POST`)
        - web browser - client => view function should return HTML to give well-formatted data
            - view uses template and insert certain data in placeholders marked with tags inside a template
    - **Function based view**
    ```Python
    from django.shortcuts import render

    def myview(request):
        if request.method == "GET":
            # perform read or delete
        
        if request.method == "POST":
            # perform insert or update
            context = {}
        
        return render(request, 'template.html', context)    # render a template with passed context
    ```
    - **Class based views** - can logically divide get and post method functionality
    ```Python
    from django.views import View
    class MyView(View):
        def get(self, request):
            return HttpResponse('response to GET')
        
        def post(self, request):
            return HttpResponse('response to post')
    ```
    - Generic views `django.views.generic`
        - There are built-in views for rendering a template, showing an instance or a list of instances from db, adding or updating a model instance
        - `TemplateView`, `CreateView`, `ListView`, `DetailView`, `UpdateView`
        - Subclass the generic view and set `model` and `template_name` properties
- Creating views and view logic
    - view mapping at project.url level
    - passing html text to `HttpResponse` object

### Requests and URLs
- HTTP requests
    - HTTP - protocol to transfer webpages, images and other files
        - request-response cycle
    - http request consist of:
        - [method: get, post, put, delete] [path] [version]
        - headers: server type
        - body: with information for certain methods
    - http response consist of:
        - [version] [status code] [status message]
            - status code: Informational(100), Success(200), Redirect(300), Client-side error(400, 401, 403, 404), Server-side error(500)
    - https - encryption to packets (ssl certificate)
- Request and Response objects
    - web application works on the principle of a request-response cycle in a client-server architecture, following the HTTP protocol.
        - web browser makes a request and web application response according to request
    - `HttpRequest` `HttpResponse` objects `django.http` module
        - `HttpRequest` provided by the server. URL dispatcher invokes mapped view and passed HttpRequest object as first argument.
            - `request.method` : GET(retrieve), POST(insert), PUT(update), DELETE(delete)
                - `REST`
            - `request.GET and request.POST` - dictionary with key:value parameters of the request
            - `request.COOKIES` - dictionary string:value
            - `request.FILES` - `UploadFile` objects
            - `request.user` - user object. `AnonymousUser` when not `.is_authenticated()`
            - `request.has_key()` - to check if POST or GET arguments has key
        - `HttpRequest` class is instantiated in the view.
            - bold text can be returned or `django.template.loader` can be used to load a template
                - `get_template(path)`, `template.render(context, request)`
            - `status_code` `__get_item__` `__set_item__` get and set header, `write()` - create a file-like object
- Creating Requests and Responses
    - request: `path_info` `path` `address` `scheme`
    - response object: `content-type='text/html'` `charset='utf-8'`
- Understanding URLs
    - `http://www.littlelemon.com/menu/2020`
        - scheme: `http://` or `https://`
        - subdomain: `www`
        - domain name
            - second level: company identifier
            - top-level: country or group (org, com, ie)
        - path `menu`
        - parameters `2020`
            - Url parameters most used in django
            - Query parameters `address?par1=val1&par2=val2`
    - URL design
- Parameters
    - Path parameters parsed by url dispatcher
        - `path('path/<par1>/<par2>', view)`
            - `str, int, slug, uuid, path` types
            - `<str:name>/<int:age>/`
        - `def view(request, par1, par2)`
        - view argument names should be matched with path parameters names
    - Query parameters
        - `url?par1=val1&par2=val2`
            - `?` - endpoint
        - not parsed by URL dispatcher. `request.GET` dict to retrieve parameters
    - Body parameters - `post` method
        - Using html form to make `post` request and then retrieve data from request body using `request.POST` dictionary
        - showform, getform views to send data and retrieve them and show result
        - csrf_token - prevent cross-site forgery attacks
- Mapping URLs with path params `<type:name>` and **path converters**

- [Additional Resources](https://www.coursera.org/learn/django-web-framework/supplement/S9v2H/additional-resources)

### Creating URL and Views
- Regular expressions with URLs
    - RegEx - universal. A way to identify pattern
    - `re_path` function to use regular expression
        - `r'^menu_item/([0-9]{2})$'`   - raw string
        - `^` - start of a string, `$` - end of a string
        - `()` - group RegEx. `[]` group of valid symbols. `{}` exact number of symbols 
- **URL namespacing and views**
    - it's a bad practice to **hardcode** urls to views. `name` argument of `path` function can be used to retrieve url
    - F.e. `django.urls - reverse('index')`. But there may be a problem when we have several apps with same view names. Thus namespaces are neede
        - Application namespace - creating `app_name` variable inside `urls.py` 
        - Instance namespace - pass `namespace` argument to `include` function when connecting project urls to app urls
            - Now url can be retrieved as `reserve('app_name:view_name')`
            - Or in template as `{% url 'app_name:view_name' %}`
- Error handling
    - Common errors
        - 400 (bad parameters), 401 login, 403 permissions, 404 not found
        - 500 internal server error
    - Exceptions
    - Error handling views - added separatly (project level)
        - handler 400, 403, 404, 500
        - urls.py - `handler... = 'path to view'`
        - Default views (BadRequest, PermissionDenied, PageNotFoundView, ServerErrorView)
        - HttpResponse classes with status codes (`HttpResponseNotFound` etc)
    - Practice
        - `HttpResponse(..., status_code='404')` or `HttpResponseNotFound`
            - in the 2nd usage, django internally sends 404 => appropriate 404 page can be configured. In the 1st usage, default 404 view displayed
        - 404 - incorrect url
            - `Http404` exception - raise for standard error page
            ```Python
            def detail(request, id):
                try:
                    product = Product.objects.get(pk=id)
                except Product.DoesNotExist:
                    raise Http404("Product does not exist")
                return HttpResponse("Product Found")
            ```
        - Custom error page
            - `404.html` in `project/templates` folder
            - `DEBUG = False` to not see error's traceback
        - Exception classes `django.core.exceptions`
            - `ObjectDoesNotExist`, `EmptyResultSet` (query return noting), `FieldDoesNotExist`, `MultipleObjectReturn` (when 1 object expected but many returned), `PermissionDenied`, `ViewDoesNotExist` (incorrect mapping URLConf)
                ```Python
                try:
                    field = model._meta.get_field("name")
                except FieldDoesNotExist:
                    return HttpResponse("Field doesn't exist")
                
                if not request.user.has_perm('myapp.view_mymodel'):
                    raise PermissionDenied()
                return HttpResponse()
                ```
            - POST, PUT request. Django field types `EmailField`, `FileField`, `IntegerField`, `MultipleChoiseField`. Fields has built in validation `is_valid`
                ```python
                if request.method == "POST":
                    form = MyForm(request.POST)
                    if form.is_valid():
                        #
                    else:
                        return HttpResponse("Submitted form is invalid")
                ```
    - Demo
        - `Debug mode` - custom errorpage or with tracebacks
        - Creating custom project-leve view `handler404` and `handler404` variable in project.urls with full path to view function
        - Using `HttpResponse` or `HttpResponseNotFound`
- Class based view - use views as objects. Callable
    - methods CRUD (get, post, put, delete) in class => remove conditionals in functions
    - OOP techniques (**mixins**, multiple inheritance)
        - Mixins: Create, List, Retrieve, Update, Delete - generic views?
        - Use carefully

### Module Summary
- Creating views, Request and response cycle, http methods
    - What is view?
    - View function, Routing
        - Process data, Retrieve data, Transform, Rendering
    - urls.py
    - creating and mapping views
    - DRY
    - Request and Response objects and its attr
    - View namespaces
    - Parameters - Path or Query or Body
- RegEx, Map urls, Handle Errors
    - RegEx
    - Error types and error handling
- Class based views and reusability
    - OOP techniques
    - Class methods = http methods

- [Additional resources](https://www.coursera.org/learn/django-web-framework/supplement/8VHUC/additional-resources)


## 3 WEEK: Models
### Models and migrations
- Models - Data Layer (Presentation, Application, Data)
    - Object equivalent of a db table. Definitive source about data
        - maps to a single table
        - Have needed fields and behavior
    - 2 Ways
        - Creating db and populate and use custom queries in application level
        - Use a framework (ORM) - replaces custom queries by providing database-access api
    - subclass of `django.db.models.Model`
        - attributes - fields of a database
        - id created by default
        ```python
        class User(models.Model):
            name = CharField(100)
            surname = CharField(100)
        ```
    - CRUD
        - C: Create class object and `instance.save()` method
        - R: `model.objects.get(pk=id)` method
        - U: get object, change its attribute, save it
        - D: `model.objects.filter(cond).delete()` method
    - Creating model class => Migrations (create tables using models)
- Model relationships
    - relationship types
        - One to One: `OneToOneField(model, on_delete=model.CASCADE)`
        - One to Many: `ForeignKey(...)`
        - Many to Many: `ManyToManyField(model)`
    - FieldTypes
        - `EmailField(max_length)`, `CharField(max_length)`, `IntegerField(max_length)`, `URLField()`
        - `primary_key` key argument if you want custom pk
    - on_delete option
        - `CASCADE`, `PROTECT`, `RESTRICT`(exception protect)
- Creating models
    - Create model for menu item
    - Migrations `makemigrations` `migrate`
    - django shell to access database
        - `model.objects.create(key=value)` method to create without saving
        - `.all()`, `.get(pk=id)`
    - `__str__` method to have better representation
- Migrations
    - PostgreSQL, MySQL, SQLite
    - ORM - relate class to sql table
    - Sometimes need to alter table (add new col, rename col, delete col) => migrations
    - No sql => just altering model class
    - Sync, Maintanence, VCS
        - Migration scripts kept in repo
        - Easier for development team (not creating sql, where to store files etc)
    - VCS to database
    - How to use?
        - CLI commands
            - create migration script - set of instructions to db `makemigrations`
            - apply migrations `migrate`
            - `sqlmigrate app migration_script` - shows sql query for migration
            - `showmigrations` - information about migration status and what is changed
        - Migrate default `INSTALLED_APPS` tables (`auth module`) by running `migrate`
        - Creating app
            - Inside an app there is a `migrations` folder with migration scripts
            - creating model -> run `makemigrations` command -> new migration script created in migrations folder -> run `migrate` command to apply migrations.
        - VCS
            - modifying model by renaming model -> makemigrations -> add new field -> makemigrations again => 2 new migration scripts -> `showmigrations` -> `migrate`
            - `python manage.py migrate app migration_id` - to roll back **!!!!**
    - Working with migrations
        - Creating model -> `py manage.py makemigrations` -> creating migration script in migrations folder -> `migrate` to apply them.
        - Revert back using `py manage.py migrate appname migr_name [--plan]`
        - `showmigrations` to see infromation about migrations
        - `sqlmigrate` to see sql query that will be executed by migration
- History of changes of migrations
    - Migration folder
        - migration scripts - 2 lists
            - python code
                - dependencies - previous migrations
                - operations - actions to perform
                    - CreateModel, DeleteModel, AddField, AlterField, AddIndex
        - `showmigrations`
        - django-migrations tables
            - ID APP name datetime
        - Migrations can be applied to a specific app
- Foreign Keys in models
    - MenuItem and Cuisine(MenuCategory) example
    - ForeignKey(Model, on_delete=models.Protect, default=None)
    - admin register models - app level admin.py -> admin.site.register(ModelClass)
    - ensure app config (settings)
    - makemigrations -> migrate
    - `related_name` parameter to change name in the sql table
- ORM
    - ORM - Object Relation Mapping - tool that helps to interact with SQL via code
        - maps a class to a table   (`Model`)
            - attribute - table 
        - Performs CRUD
        - Migration mechanism
    - QuerySet
        - Create, `save()` method or using **manager of the model** `model.objects` and `create()`
        - creating objects with foreign key object
        - `manager.all()`
        - `manager.filter(criteria)`
            - criteria `name__startswith="H"`
        - Update: retrieve object -> change attr -> `save()`
        - Delete: retrieve object -> `object.delete()` method
- Using ORM
    - QuerySet - collection of objects
    - QuerySet API
        - get = select
        - filter = where
        - & operator
        - Methods and operator returns queryset
        - methods doens't return query set
    - Example
        - & method between two filters - and operator
- [Additional Resources](https://www.coursera.org/learn/django-web-framework/supplement/kbX1B/additional-resources)


### Models and Forms
- Forms - tool to collect data from user. (Login, Create, update)
    - Types
        - Class Form
        - Model Form - create form from model
    - Django forms automatically create html tags. forms.py file
    ```python
    from django import forms
    class MyForm(forms.Form):   #class form
        field = forms.CharField(label="...", max_length=100)
    
    class MyModelForm(forms.ModelForm):
        class Meta:
            model = Model
            field = [fields]
    ```
    ```html
    <form ...>
        {{ form }}
        <input type="submit" value="OK">
    </form>
    ```
- Django form fields and datatypes
    - Input, Radio, Drop-List, Checkboxes
    - fields
        - CharField, EmailField, IntegerField, MultipleChoiseField, FileField
    - arguments
        - `label`, `required` by default, `initial` value, `help_text` descriptive text
        - CharField `widget=formsTextArea(attrs={'rows':5})`
        - EmailField
        - DateField `widget=NumberInput(attrs={'type':'date'})`
        - ChoiceField(choices=list(tuples)) `widget=RadioSelect
    - Validation
- Django fields
    - Model - class that matches with table via ORM. So methods can be invoked instead of sql queries
        - How to create a model => subclasses?
            - `appname_modelname` - default table name => `db_table` parameter in `Meta` nested class to change
    - From fields
    - Field properties
        - `primary_key`= False by default => custom pk field. Otherwise integerfield created
        - `unique` - boolean to ensure uniqueness
        - `choices` - two item tuples with a drop-down
    - Field Types
        - CharField(max_length) - TextField
        - IntegerField - SmallIntegerField, AutoField, BigIntegerField for different min, max
        - FloatField - DecimalField
        - EmailField - CharField with email validator
        - FileField - `upload_to` parameter for designated place
        - ImageField - FileField with image validator
        - URLField - CharField with url validator
        - DateTimeField - `datetime.datetime` object. DateField - `datetime.date` object
    - Relationship fields
        - ForeignKey(model, on_delete)
        - OneToOneField(...)
        - ManyToManyField(model)
        - `on_delete` property
            - CASCADE
            - PROTECT - protects referenced object from deletion
            - RESTRICT - same as protect but allows to delete if all referenceb objects will be deleted with cascade property (artist, album, song example)
- Form API
    - Forms required to get data from user - HTML page
        - `text` `select` etc
    - `forms.Form` class to create custom forms that will automatically create HTML
        - Fields `forms.Field`
            - `CharField` = text, `label` and `max_length` properties
                - `widget=forms.TextArea` for longer text
                - `EmailField`
            - `ChoiceField` = Select. `choices` property with pairs. `max_length` property
            - `IntegerField` - `min_value` `max_value` properties
            - `FloatField` `DecimalField`
            - `FileField` - `upload_to` property. type=file
                - `ImageField` - **Pillow** library
    - Form Template
        - Creating a template: `csrf_token`; `form` `table` tag should be written by a coder
            - `form.as_table` - default. `.as_p` `as_ul` `as_div`
        - Render a template in a view passing `form` object in context.
    - View processing request
        - Post data check
        - creating form with data
        - `is_valid` and `cleaned_data` attr
    ```python
    # forms.py
    from django import forms    

    class ApplicationForm(forms.Form): 
        name = forms.CharField(label='Name of Applicant', max_length=50) 
        address = forms.CharField(label='Address', max_length=100) 
        posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
        field = forms.ChoiceField(choices=posts) 
    
    # views.py   
    def index(request):  
        if request.method == 'POST': 
            form = ApplicationForm(request.POST) 
            # check whether it's valid: 
            if form.is_valid(): 
                # process the data  
                # ... 
                # ... 
                return HttpResponse('Form successfully submitted') 
        else:
            form = ApplicationForm()
        return render(...)
    ```
    ```html
        <html>
        <body>
            <form action="/form" action="POST">
                {% csrf_token %}
                <table>
                    {{ f }}
                </table>
        </body>
        <html>
    ```
- Creating forms
    - Creating a form in `forms.py`
    - Creating a view with just rendering a form
    - Creating a template (form tag, submit input, and {{form}})
    - csrf_token - form data safe
    - Making `as_p`
    - `required`, `help_text` parameteres 
    - adding styles to form tag through attribute
- Model form
    - Creating a model
    - `ModelForm` class
        - `Meta` nested class with implementation settings (`model`, `fields`)
            - `fields = ['field1', 'field2'...] or '__all__'`
        - `form.save()` to save data in form to the model table
    ```python
    #   models.py
    class MyModel(Model):
        field = ...
    
    # forms.py
    class MyForm(ModelForm):
        class Meta:
            model = MyModel
            fields = '__all__'
    
    # views.py
    def my_view(request):
        if request.method == 'POST':
            form = MyForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = MyForm()
        return render(...)
    ```

### Admin
- Django admin
- Managing users, Adding group of users
- Permissions


### Database configurations
- Database options
- MySQL


## 4 WEEK: Templates
### Templates
- Templates
- Example
- Creating templates

### Workng with templates
- Working with templates
- Language and Variable interpolation
- Dynamic templates in Django
- Mapping model object to a template
- Template inheritance
- Working with template inheritance

### Debugging and Testing
- Debugging django applications
- Testing in Django
- 