# Description
Capstone project course from Meta Back-end Developer specialization


## 1 Week: Starting the project
### Project info
- Introduction
    - Scenario: Little lemon restaurant
        - Table reservation functionality
    - Build an API
    - Process of building an app
    - 4 modules
        1. starting
            - config, github project, django project, urls&routes, static routes
        2. project functionality
            - Creating db schema models, DRF api menu api - list of food menu items
            - mysql connection
        3. security and testing
            - Authentication, login, registration, logout, security of API
            - testing, unit testing, insomnia
        4. project assessment
            - self review, peer review
- Environment
    - pipenv shell
    - django, djangorestframework, djangorestframework-xml, mysqlclient
    - **How to install and bundle front end tools?**
- [Additional resources](https://www.coursera.org/learn/back-end-developer-capstone/supplement/gw1zC/additional-resources)


### Setting up a project
- Setting up a project
    - coding environment (python, vscode, virtual environment (venv, pipenv, activation), django)
    - `django-admin` utility, `manage.py` file
    - Command: `startproject`, `runserver`, `startapp`
        - register app
    - push to github
        - creating blank repo in github
        - Gitbash -> django project folder -> git init command -> commit -> set remote -> push
- Recap: VCS
    - Collaboration, Branching, Workflow
    - Centralized, Distributed
    - Git
        - config credentials
        - git init, commit, status, add, restore, branch, checkout
    - Github - service to store git repositories
        - creating repo, git remote, push, clone
- **Exercise: Setting up the repository**
    1. Download git
    2. Sign up for github, create *`LittleLemon`* repository
    3. open git bash, copy url
    4. `mkdir` for a project directory, `cd` into it
    5. `git clone` repo
        - [submodules](https://gist.github.com/gitaarik/8735255)
    6. cd repo, ls -la
    7. set git credentials
    8. create a file, commit it, push it
    9. edit file on github, pull it
- Recap: Django set up
    - Installing python and vs code.
    - Setting up a virtual environment
        - `venv` module of python standard library
            - activating
        - `pipenv`
    - Installing `django`, `djangorestframework`, `mysqlclient`
    - Creating a django project
        - `django-admin starproject littlelemon .`
    - Launching the development server
        - `python manage.py runserver`
- **Exercise: Setting up the Django project**
    - Build two apis - order food and book table.
    1. Install python and vscode.
        - extensions: python
        - interpreter: `ctrl+shift+p` to choose interpreter in vscode
    2. Create a python virtual environment, install everything needed
    3. Create a project `django-admin starproject littlelemon .`
    4. Create an app restaurant `python manage.py startapp restaurant`
        - add to installed apps
    5. Start the server `python manage.py runserver`
- **Exercise: Committing the Project**
    1. Create a new branch `git checkout -b branchname`
    2. Commit everything to this branch `git add .` `git commit -m 'message'`
    3. push it `git push -u origin branch`
    4. Create a pull request and merge branches
    5. `git pull` on master branch to update locally
- [Additional resources](https://www.coursera.org/learn/back-end-developer-capstone/supplement/MYoJb/additional-resources)

### Static Content
- What do you know about URLs and Routes
    - Client (browser or curl) sends request with some HTTP method.
    - URLConf helps to handle a request
        - `ROOT_URLCONF` setting
        - Django matches url with a url patterns defined in the URLConf
            - imports an associated view
            - or 404
        - `urls.py` module at app and project level.
            - `urlpatterns`
                - each `path` function defines a **route** and binds a path to a view function
                    - view function to process a request and parameter and then return HttpResponse or render a template.
                    - Url Dispatcher sends request object and other parameters to the view function
            - url path
                - Parameters
                    - path parameters
                    - query parameters
    - Static content (JS, CSS, HTML, Images)
        - settings
            - `STATIC_URL` - `static` usually
            - `STATICFILES_DIRS`
        - dtl
            - `{% load_static %}
- Recap: Django routes
    - Django model. MVT + URL Dispatcher
        - URL Dispatcher = Controller = `urls.py` module
            - defines url patterns mapped with a view function to be invoked.
            - `path` function constructs the route
    - Create a restaurant app
        - `views.py` - defines functions
            - `HttpResponse` or `render`
        - `app/urls.py` - view function to url pattern
        - `project/urls.py` - include urls from app to project.
        - configure installed apps
- **Exercise: Setting up the static routes**
    - DTL helps to render web pages.
    - Default project installs the `staticfiles` app
    - Static files assets are given by the course.
    1. Create `templates` dir inside `BASE_DIR`
        - Include it to `settings.TEMPLATES.DIRS`
    2. Create `index.html` inside a templates folder with
    ```html
    <html>
    <head>
        <title>Capstone Project</title>
    </head>
    <body>
        <h1 style="text-align:center;">Welcome ToLittleLemon Restaurant</h1>
    </body>
    </html>
    ```
    3. Define `index` view without parameters and context
        - map it at app level `''` and project level `'restaurant/'`
    4. Run the server and visit home page
    5. All static assets add to **restaurant/static/restaurant** folder
    6. load static files inside **index** template and add an img **littlelemon.png** using `static` tag with path `{% static 'restaurant/littlelemon.png' %}`
    7. Refresh the home page to see logo **littlelemon.png**
    - Issues
        - There was no file with name **littlelemon.png**, I used **logo.png**
        - The template and picture in the assets were different

- Questions
    - How does django search and load static files and templates? Learn in detail.

- Tips
    - Developer must decide which URL patterns they'll expose to the user and which function will be executed

### Module Summary
- Set up coding environment
- Django project, static content, static routes
- [Additional Resources](https://www.coursera.org/learn/back-end-developer-capstone/supplement/fgEe5/additional-resources)

- Quiz


## 2 Week: Project functionality
### Models and Stored procedures
- Working with database and models `models.py`
    - Model - data layer. `django.db.models.Model`
        - attributes represent db fields
        - maps to a database table
    - ORM - interacting with db in OOP manner
    - Migrations `makemigrations` `migrate` commands
        - migration scripts
        - migrations history
    - Django shell to interact with model 
        - CRUD using QuerySetAPI
    - registering model to admin site
- Recap: Django Database Configuration and Models
    - DB config
        - PostgreSQL, MariaDB, MySQL, Oracle, SQLite supported by Django
        - Other db with third-party libraries
        - `settings.DATABASE`
            - backend engine
            - credentials
            - name, address, port
        - Using another db
            - DBAPI-compatible driver required `mysqlclient` f.e.
    - Using MySQL
        - install `mysqlclient` driver
        - Configure `settings.DATABASE`
            - change backend engine
            - add db related info for connection
                - `name` of db
                - `host` `port`
                - `username` `password`
                - options
                    ```python
                    'OPTIONS': {  
                            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
                        }  
                    ```
            - Other important configuration settings
                - `CONN_MAX_AGE` - max lifetime of connection (`None` - unlimited)
                    - 0 - close after request processing
                - `AUTOCOMMIT` - Django transaction management (False to implement your own)
                - `OPTIONS` - extra parameters used when connecting to the database
                    - `'init_command': "SET sql_mode = 'STATIC_TRANS_TABLES'"` - handles invalid or missing values from being stored in db
        - Example of having credentials in different file using `OPTIONS`
            ```python
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'OPTIONS': {
                        'read_default_file': '/path/to/my.cnf',
                    },
                }
            }


            # my.cnf
            [client]
            'NAME': 'my_database'
            'USER': 'root'
            'PASSWORD': 'your_password'
            default-character-set = utf8
            ```
    - Using multiple db
        - default and other
            ```python
            DATABASES = {
                'default': {config},
                'mydb': {config}
            }

            ```
- **Exercise: Setting up the MySQL connection**
    1. Install mysql server, 3306 port number
        - start using `mysql -u root -p` and type credentials
        - Create 'LittleLemon' database
    2. Activate virtual environment and install `mysqlclient`
        - `pip install mysqlclient` `pipenv install mysqlclient`
    3. Go to `settings.py` and add mysql configuration instead of sqlite
        ```python
        DATABASES = {
            'default': {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "LittleLemon",
                "USER": "root",
                "PASSWORD": '',
                "HOST": "127.0.0.1",
                "PORT": "3306",
                'OPTIONS': {   
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"   
                }   
            }
        }

        # OR using options file
        DATABASES = {
            'default': {
                "ENGINE": "django.db.backends.mysql",
                'OPTIONS': {
                    'read_default_file': '/path/to/my.cnf',  
                }   
            }
        }
        # Like in notes
        # In documentation
        [client]
        database = NAME
        user = USER
        password = PASSWORD
        default-character-set = utf8
        # ssl, init_command, sql_mode parameters
        # host, port
        ```
    4. Install mysql extension to vscode
        - VSCode configuration
            - Mysql section can be seen in the vscode window
                - click `+` and connect to mysql server
    5. Migrate and check in vscode that tables are created
- **Exercise: Setting up the models**
    - Create Menu, Booking models and migrate them
    - Booking table
        - ID - int(11)
        - name - varchar(255)
        - No_of_guests int(6)
        - BookingDate datetime
    - Menu table
        - ID - int(11)
        - Title - varchar(255)
        - Price - decimal(10, 2)
        - Inventory - int(5)
    1. Declare menu and booking models
    2. makemigrations migrate
    3. register models to admin
    4. Create superuser and login to the admin.
        - Credentials `admin` `littleLemon@876!`
        - Add some data to Menu and Booking models using interface
    5. Check the data in vscode
    - Questions
        - how to make int(6) or int(5) using django orm?

- Some info
    - default table name appname_modelname
    - `app/migrations` - folder with migration scripts
    - `sqlmigrate` command
    - how to roll back with migrations? `migrate app migrationid`
- [Additional resources](https://www.coursera.org/learn/back-end-developer-capstone/supplement/Z4TxE/additional-resources)

### Adding APIs
- Building an API
    - Templating - dynamic content with html response
    - API returns json or xml response
    - DRF - wrapper of django
        - converts models into json, serializes, renders
    - Steps to build REST APIs with CRUD operations
        1. Install `djangorestframework` tool and add `rest_framework` to installed apps
        2. Check created models (or create them) and add model serializers in `serializers.py` file.
            - serializer(items, many?)
        3. Create views to handle different http methods
            - class based `APIView` class or generics
            - function based `@api_view` decorator
            - Response object `serializer.data`
        4. Map views to endpoints at app level and include urls at project level
        5. Check with http client (Insomnia, Postman, HTTPie)
- Recap: Django Rest Framework
    - Steps to configure rest framework app. creating `users` app
        1. Create environment
        2. Create project and app, add superuser, migrate, runserver
        3. Declare `UserSerializer` with `['url', 'username', 'email', 'groups']`
        4. Create views
            - types: function, class, mixins, generic, viewsets
            - `UserViewSet` class creation
                - `permission_classes` add `IsAuthenticated`
        5. URL configuration using `DefaultRouter` class instead of declaring
        ```python
        router = routers.DefaultRouter()  
        router.register(r'users', views.UserViewSet)  

        urlpatterns = [  
            path('', include(router.urls)),  
            path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))   # to use browsable api
        ]
        ```

- **Exercise: Set up the menu API**
    1. install rest framework and add it to installed apps
    2. Create `MenuSerializer` as subclass of ModelSerializer class in `serializers.py` module
    3. Declare generic views for Menu model
        - MenuItemView - `ListCreateAPIView`
        - SingleMenuItemView - `RetrieveUpdataAPIView` `DestroyAPIView`
    4. define url routes and include `restaurant/menu/`
        - `items`
        - `items/<int:pk>`
    5. Check if everything works
    - Question
        - Why to use `RetrieveUpdateAPIView` `DestroyAPIView` separately but not `RetrieveUpdataDestroyAPIView`?
        - Naming conventions for routes names in path function
- **Exercise: Set up the table booking API**
    1. Ensure that rest framework installed and added to installed apps
    2. Create serializer for Booking model with all fields `BookingSerializer`
    3. Create `BookingViewSet` class inheriting `ModelViewSet`
        - set queryset and serializer_class
    4. Open urls.py in project level
        - import `rest_framework.routers.DefaultRouter`
        - use `register(path, viewset class)` method to register route
        - endpoint `restaurant/booking/tables`
            - `tables` in route
            - `restaurant/booking/` in urlpatterns
    5. Check
    - Question
        - How to create different routes for different apis? (Conventions)
        - How router works and why I don't need to create any endpoint with pk for viewset?
        - Read about DefaultRouter class

### Module Summary
- Connect the back-end to the database
    - models and stored procedures
    - configure db settings to connect mysql
- Implement the menu and table booking apis
    - using DRF to create apis
        - model -> serializer -> view -> url patterns
- [Additional resources](https://www.coursera.org/learn/back-end-developer-capstone/supplement/LltAT/additional-resources)

- Quiz

## 3 Week: Security and testing

### User Authentication
- Securing your app
    - Session based
    - Authenticate requests
    - Authentication schemes
        - remote user
            - BasicAuthentication scheme
                - Signed agains user's username and password
                - Appropriate for testing
                - request.user
                - request.auth
        - session
            - SessionAuthentication Scheme - 
                - Django default session-backend for authenticaion
                - Appropriate for AJAX clients
        - token-based - client server setups (native desktop and mobile clients)
            - `rest_framework.authtoken` app
                - migrate
                - creating
                    - admin panel
                    - `Token.objects.create(user=)`
                - use Bearer `Token token`
                - @permission_classes([IsAuthenticated])
                - `settings.REST_FRAMEWORK.DEFAULT_AUTHENTICATION_CLASSES`
                    - `rest_framework.authentication.TokenAuthentication`
                - `rest_framework.authtoken.views obtain_auth_token`
                    - get credentials
                    - add routes `api-token-auth`
- Recap: User Authentication
    - Intro
        - basic session-based authentication - needed certain middleware
        - Token-based
    - Steps
        1. Enable token authentication
            - `rest_framework`, `app`, `rest_framework.authtoken` to installed_apps
                - migrate
        2. Ensure MenuItem model
        3. Serializer for menuItem model
        4. Create generic class-based views (ListCreate, Retrieve...)
        5. Declare urls `api/menu-items` `api/menu-items/pk`
        6. Authentication
            - `@permission_classes([IsAuthenticated])` for function based views
            - user bearer token and create a view to access it via token
            - or obtain using `api/api-token-auth` endpoint with obtain_auth_token view
            - `permission_classes` attribute inside class based views
- **Exercise: Add the registration page**
    - Goal: be able to add new users and modify existing
    - Using `Djoser` library - easy to login, register, logout
    1. Install `djoser` and add to installed apps after rest_framework
    2. add to settings.py `DJOSER = {"USER_ID_FIELD":"username"}`
    3. Check `REST_FRAMEWORK` setting with `TokenAuthentication` and `SessionAuthentication` added to the `DEFAULT_AUTHENTICATION_CLASSES`
        - Add `rest_framework.authtoken` app
    4. Enable djoser urls `auth` `djoser.urls` `djoser.urls.authtoken`
    5. Run migrations and check for `Tokens` table in admin panel
    6. Visit users list endpoint and add a new user
    7. Go to `auth/token/login/` from djoser to generate new token
    8. Logout by going `auth/token/logout/`
    - Questions
        - Read fully about djoser library
        - How to create everything by django and drf
- **Exercise: Securing the table booking API**
    1. Add `rest_framework.authtoken` to installed apps
    2. import `rest_framework.permissions.IsAuthenticated` in views.py
    3. add permission_classes with permission above to BookingViewSet
    4. add to app urls `rest_framework.authtoken.views.obtain_auth_token` view with `'api-token-auth/'` endpoint
    5. Go to insomnia and obtain token
        - make a request to booking api without and with **Bearer** token
    - Issues
        - Routes are kind of strangely configured according to exercises from the course.
- Knowledge check
    - default permission policy!
    - JWT configuration
- [Additional Resources](https://www.coursera.org/learn/back-end-developer-capstone/supplement/WEZOz/additional-resources)

### Testing the api
- Testing your application
    - What to test
        - Request handling
        - Form validation and processing
        - Template rendering
    - Steps
        0. Create project and app inside it
        1. Install rest framework and add to installed app
        2. Create model => register to admin => add instances
        3. Create serializer
        4. Create views => map urls
        5. Test views using Browsable api view or insomnia client
        6. Or create unit tests using `django.test.TestCase`
            - define function with assertion test_name
            - `python manage.py test`
- Recap: Unit Testing
    - TDD adopt
    - Prerequisites
        - install django and rest framework
        - Create project and an app
        - add rest framework to installed apps
        - migrate
    - Model => serializers => views
- **Exercise: Adding unit tests**
    - `test_models.py test_views.py` files
    - Steps
        1. Delete `test.py` file from app. Create tests folder in project container folder.
        2. Add `str` method to Menu model with format `title : price`
        3. create test_models.py
            - Import `TestCase` from django.test
            - Declare MenuTest
                - define `instance` method that adds a new instance to Menu
                - Call self.assertEqual that compares string representation with expected
        4. run tests `python manage.py test`
        5. create and opent test_views.py
            - Write `MenuViewTest` with `TestCase` base class
            - Use setup method to add a few test instances of the `Menu` model\
            - add test_getall to retrieve all added menu instances
            - check if serialized data equal to the response
        6. run tests again
    - Questions
        - How test runner searches for tests? Especially in packages
        - How to add names to urls for namespacing using DefaultRouter?
    - Issue
        - Test runner couldn't find tests inside `tests` folder, so I added `__init__.py` file inside it and it worked.
        - tests folder creted in base dir but have to be created in project. Not clear instruction in the task!
- Recap: Testing your API
    - Insomnia usage to test api endpoints
    - Prerequisites
        - Created menu api
    - Insomnia
        - Install and run
        - Make sure application is running
        - aquaint yourself with the interface
        - Create a request to get single menu item
- **Exercise: Testing the API using Insomnia**
    1. Downlaod insomnia and run
    2. Run project and check it in browser
    3. Create requests
        - get request to get menu items
        - Post request to create a new menu itme using json
        - put request to update existing item
        - delete request or an item
- Knowledge check

### Model Summary
- Setup user registration and authentication
    - Authentication schemes
    - registration, login, logout
- Test with unittest and insomnia
    - unit test framework
    - insomnia rest client
- [Additional Resources](https://www.coursera.org/learn/back-end-developer-capstone/supplement/QVFa8/additional-resources)


## 4 Week: Final Grade
- Course Recap
    1. Starting the project
        - composing, django to serve static html, commit to git repository
        - set up a repo, project, commiting, static routes and content
    2. Connecting to db and imlementing menu and table booking api
        - setting up mysql connection, models
        - querying the stored procedures, setting up the menu and table booking api
    3. Security and testing
        - Authentication and authorization
        - insomnia testing
        - Adding registration, login, logout functionality, table booking api, unit tests, testing api usign insomnia

- Final touches to capstone project

