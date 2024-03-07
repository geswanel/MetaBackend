


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
- Views
- CReating a view and mapping urls
- creating views and view logic

### Requests and URLs
- HTTP requests
- Creating requests and responses
- Understanding URLs
- Parameters
- Mapping URLs with params

### Creating URL and Views
- Regular expressions with urls
- URL namespacing and views
- Error handling
- Class based view

## 3 WEEK: Models
### Models and migrations
- Models
- Model relationship
- Creating models
- Migrations How to use migrations
- History of changes
- Foreign Keys in models
- ORM

### Models and Forms
- Forms
- Django form fields and datatypes
- Django fields
- Form API
- Creating forms
- Model form

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