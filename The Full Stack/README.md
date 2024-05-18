## 1 WEEK: Introduction to the full stack

### Intro to course
- APIs infrustrucure
- Fullstack - end to end develoment
- Little lemon
    - API, backend, databases
    - Front end infrustructure
- Curriculum
    - Module1 - fullstack developer. N-tier architecture
    - Module2 - HTML, CSS, JS
    - Module3 - Django for Fullstack
    - Module4 - Production environments and hosting solutions, cloud computing
    - Final project
- A day in the life
    - A lot of communication, collaboration
    - Design documents and feedbacks
    - Move fast, On the same page
    - a lot of extra step
    - Engineer -> Team leader
    - Task based work -> Drive more projects


### Intro to Full stack
- What is full stack development?
    - Stacks? - combination of software
        - Front-end - user interface. HTML, CSS CSS framework, JS and React,
            - Web, Mobile
            - iOS, Android
        - Back-end - Application core. Python Django DRF, Data management system, db
            - Business logic, workflows, data
            - Build tools, db, caching apps
        - Data stack
            - SQL, NoSQL (MySQL, MariaDB, PostgreSQL)
            - Caching (Redis)
    - The Full Stack - equally skilled in every stack
        - Understand a complete project
        - Appropriate tool selection
        - UI, responsive, graphics
        - optimizations
        - security
        - API
        - Backend
        - DB
        - SErver processes
        - CI/CD workflows
    - DevOps skills
        - prod, stage, development servers
    - Version Control: Git
- N-tier architecture
    - UI, Backend, Business logic, db
    - Architectures
        - Layers and Tiers
            - Presentation, core, db
                - On different servers, physical separation => tiers
                - virtual separation => layers
    - N-tier applicatoin
        - 3-tier
            - Presentation tier
                - Thin Clients, communicate with app, present data
            - Application tier - code
            - Data tier - db
            - Example
                - code and db => two tier
                - client computer => 3rd tier
        - 4-tier
            - \+ Delivery tier
                - Caching and delivering front-end assets.
                - CDN providers => store html css js images and deliver to the client from the nearest server
    - Security, Scalability, Maintanence, Improvement
        - More efficient
- Client- server architecture
    - client
        - thin clients - don't apply the business logic
        - thick clients - do heavier data processing on the client side
    - server
        - Holds the application core, business logic, data processing
        - cloud computing units, containers, vm, servers.
    - Simultanious handling multiple requests
    - Communication - HTTP, Websocket
    - Advantages - separate layer
        - multiple clients
        - scaling, optimizing, securing easier
    - Disadvantages
        - management

### Module Summary
- Full stack development
- Stacks
    - Python Django DRF - back end
    - Full stack - core, process data, present api, databases, servers, 
- N-tier architecture
    - Benefits: security, scalability, maintenance, improvement
    - 3-tier, 4-tier
        - Presentation, Application, Data tier
        - delivery tier
- Client-server architecture

- [Additional Resources](https://www.coursera.org/learn/the-full-stack/supplement/c6i9J/additional-resources)

## 2 WEEK: Front-end technologies
### HTML
- Html and css usage
    - HTML - markup language (1990) - share information. content of document
    - CSS - stylesheet language - look of document
    - W3C organization
    - html improvements
        - Audio video
        - responsive
        - new form input tags
        - validation of form
        - text editing and spell checking
    - css
        - media queries
        - box-sizing
        - multiple background
        - border images
        - text shadows
        - transformations and transitions
    - Cross platform
- **Semantic tags** and why we need them
    - Searching, Accessibility
    - Understanding
    - Tags
        - headings, ul, or
    - Structure
        - `html`
        - `head`
        - `body`
            - `header`
                - company logo
                - `nav`
                    - `ul li a`
            - `main`
                - `section` - Individual sections of the article; Should contain headings; Describe different section of a webpage
                - `article` - complete, self-contained, independently distributable. Page in a newspaper
                    - forum post, article, blog post, user comment, interactive widget
                    - `h`
                    - `p`
            - `footer`
                - contact, social media links, additional navigation
- What is HTML
    - Frame - Structure of a webpage
    - History - browsing online to transfer scientific data. Tim Berners Lee
    - Webpage, server, `index.html`
    - Elements
        - Tags
            - opening, closing or empty
    - HTML Specification - W3C - HTML5
    - Tags
        - p, br, img
- Semantic tags in actions
    - New blog page - several block posts
    - Structure of body
        - header
            - img with logo
        - nav - navigation
            - ul li a - index, location, blog
        - main - content
            - h1 - Blog
            - article for every blog post
                - h2 - title of a blog post
                - p - blog post text
        - footer
            - p - copyright
- Forms and validation
    - Capture user input
    - How to ensure that data is valid?
        - Form validation - use both
            - Client side - JS code + immediate feedback
            - Server side - after submittion - more secure, prevent invalid submittion. More complex check, business requirements. db checks
    - Tags
        - input - included validation
            - types
                - auto validation
                    - email
                    - tel
                        - pattern attr
                    - url
                    - date
                    - time
                    - number - nl
                        - min, max attr
                    - range
                        - min, max attr
                    - color
                    - datetime-local
                - submit - no label
                    - onclick attr
                    - form handler
                - checkbox
                - radio - single
                    - name attr
                - text - single line
                - password
                - file
                - hidden - no label
                - image - no label
                - reset - nl
                - search
                - week
                - month
            - required attr
        - button
            - onclick attr
        - come with `label` - best practice
        - button
- From Submission
    - http request-response cycle
    - request methods - method attr of a form
        - GET - part of query string parameters
            - extracts data from the url
            - Disadvantages: Length limited by browser and server, security threats
        - POST - content in body of http request
            - more secure but not enough => **https!**
    - response is sent back by server
        - errors
    - Submit
        - Action - which address request sent to
            - absolute, relative, url path
        - Method - get(default) or post
            - Get - data incoded to the url
            - Post - data is sent as part of HTTP request body
        - server processes request and sends back http response.
            - JSON
- [Additional resources](https://www.coursera.org/learn/the-full-stack/supplement/UytSF/additional-resources)


### CSS
- CSS web layout
    - Visual design
    - Responsive, Flexboxes, Grids, boxes
    - Modifying
        - Fonts
        - Color
        - Layout - optimally designed with good viewport
            - `display` property - type of box
                - inline
                - block
            - box model - content, padding, border, margin
            - `flexbox` - one dim. More suitable for small scale
                - `display: flex` - float elements, positioning
                    - will arrange items in columns or row axes
                    - shrink expand
            - `grid` - two dim grid - for large scale
                - `display: grid`
        - Size
    - Viewport - browser window visible to user
- Widely used selectors
    - CSS selector chooses html element
    - Selectors
        - element
        - #id - specific element
        - .class - class attribute
        - element attribute selector
            - [attr=value] ~=, $=, *=(contains) etc
            - a[class] - links with defined class
            - a[href*="meta"]
        - element:nth-of-type(n) - nth of type
        - element:nth-child(n) - n child of html element
        - \* - all the elements - default settings reset
        - group selectors or selector stacking - comma; `el1, el2`
- CSS units of measurement
    - Absolute - when the size of a webpage will remain constant (not suitable for different viewports (devices))
        - Q, mm, **cm**, in, pc, pt, **px**
    - Relative - in relation to the other elements present inside the parent element. In relation to a viewport. **go-to** option in many cases.
        - **em** (parent font size), ex, ch, **rem** (root element font size), lh, rlh, **vw**, **vh**, vmin, vmax, **%**
- Document flow
    - Categories
        - Block - full horizontal of parent. new line
            - div, form, h
        - Inline - width and height of content - inline
            - a, img, label, input
    - Example of span and div text
- Basic **flexbox** - simple layouts
    - Dynamically align a collection of items within a container.
    - Design elements
    - Idea
        - Container and items
        - display:flex - position along the hor axis
        - positioning along axis (main, cross)
            - justify-content: center - center itmes along the main axis
                - space-between
                - other values - play around
            - align-items
        - margin - flex
        - `flex` property - responsive 
            - 1 - stretches to fill the container
    - Most common usage
        - search bar - search icon, textarea, button
            - container
                - display: inline-flex
                - overflow: hidden - clips the overflowing content
            - icon - padding
            - searchbox - flex:1 
            - searchbtn - styling
        - nav bar - highly responsive
            - container
                - display: flex
                - flex-flow: row wrap; - direction of the flex container - wrapping
                - justify-content: stretch - aligns along the main axis
            - a - inline-block
        - image gallery - reallign
            - container
                - display: flex
                - flex-flow: wrap; - direction of the flex container - wrapping
                - justify-content: space-between - aligns along the main axis
- Grids
    - columns and rows
    - Gutter - divide line between cells
    - grid cell
    - Properties
        - container
            - display: grid
            - grid-template-columns: c1size, c2size
                - `px` unit
            - grid-template-rows: r1size, r2size
                - `fr` unit
            - grid-gap
            - background-color
            - grid-auto-rows, grid-auto-columns - implicit grid
    - useful functions
        - repeat(num, val)
        - minmax(min, max)
    - Grid frameworks
        - 12 - 16 column grids
- [Grids and flexboxes cheetsheet](GridFlexboxCheatSheet.md)
- All selectors and their specificity
    - Specificity - score to resolve what rule to apply
    - Hierarchy
        1. inline styles 1000
        2. ID 100
        3. classes, attributes, pseudo-classes 10
        4. elements and pseudo-elements 1
    - Example of score calculation
        - div p.foo {} - 2 el, 1 class => 0012
    - Some others rules
        - every selector has score and place in the hierarchy
        - last written rule if specificity is the same
        - id selector if you awnt to be certain
        - universal selectors - 0 specificity
    - Cascading - counting specificity
- Pseudo class selectors
    - Select elements based on state (f.e. hover)
    - `selector:pseudo-class`
    - Classification
        - user action
            - hover
            - active - pressed button f.e.
            - focus
        - form states
            - disabled, enabled
            - checked, indeterminate
            - valid, invalid
        - specific position-based states
            - first-of-type
            - last-of-type
            - nth-of-type
            - nth-last-of-type
- Pseudo elements - specific part of element
    - `selector::pseudo-element`
    - examples
        - first-letter
        - first-line
        - selection - selected text
        - marker - bullet points for lists
        - before and after - add content before and after an element
- [Additional resources](https://www.coursera.org/learn/the-full-stack/supplement/NHUaj/additional-resources)


### JS
- Why JS?
    - Central pillar of the internet.
    - Other modifications
        - TypeScript and ..
    - Usage: Interactivity of the web page, JavaScript Framework, Node.js - server side.
    - Advantages: Easy-to-go (browser console), Accessibility, Community, Jobs, Backward compatible
    - Examples: Interactive maps, web servers
- Programming in JS
    - Learn JS basics => easily learn frameworks and libraries
    - Browser vendors => different js code for different browsers => jQuery
    - Legacy
- Variables
    - Declaring `var varName;`
    - Assigning `=`
    - printing `console.log(val1, val2)`
    - `;` to end statement. Not required but good practice
    - `+` - concatenation
- Data types
    - Knowing when to use an appropriate data type for effectiveness
    - Primitives
        - Numbers - integers and decimals
        - String - "" or ''
            - espace symbol
        - Booleans - true or false
            - Comparison operators + Logical operators to make boolean expressions
        - Null
        - Undefined
        - BigInt (es6)
        - Symbol (es6)
- Operators
    - Arithmetic: `+` `-` `/` `*` `**` `%`
    - Comparison: `<` `<=` `==` `===` `!=` `!==` `>=` `>`
        - `===` value and type
    - Logical: `&&` `||` `!`
- JS Interactivity - set of controls to define the behavior of the web pages and the browser
    - npm, node.js | angular, react, jquery, D3, Vue
    - Usage
        - Browser games
        - Form validation before submittion
        - Handle user-triggered events
        - Interact with maps
        - get their geolocation
- DOM manipulation
    - JS selectors - find a specific object in the document
        - querySelector - get first element by tag
        - querySelectorAll - get all elements by tag - list
        - getElementById - get element by id
        - getElementsByClassName - get all elements with passed class - list\
    - Change properties of objects in the web page locally
    - DOM manipulate can be made
        - browser gui
        - console using js
        - js code files for the web site
    - Example: methods and fields
        - `document.createElement('tag')`
        - `element.innerText`
        - `element.setAttribute('attrName', 'attrValue')`
        - `document.body.appendChild(element)`
- Scoping with `var`, `let`, `const`
    - global scope
    - local scope - in functions (es5)
        ```js
        function score() {
            var num2 = 20;
            console.log(num2);
        }
        ```
    - block scope - local scope inside block (es6)
        - `let` `const` - scoped to the code block where are created
        ```js
        if (color == 'red') {
            let color = 'blue'
        }
        ```
    - Standards
        - es5
            - `var` - scoped to a function or globally
            - can be used before it is declared
            - same variable can be redeclared
        - es6 - more strict behavior
            - `let`
            - `const` - never change
            - cannot use before or redeclare it
            - it's scoped to block of code
- Functions - reusable piece of code
```js
function funcName(par1, par2) {
    //body;
}

function addTwoNumbers(a, b) {
    var c = a + b;
    console.log(c);
}

//lambda
function() {
    //body
}
```
- Event Handling in JS
    - 2 ways
        - `element.addEventListener(event, func)` to the js element
        - using attribute of html element f.e. `<... onclick="func">`
            - hardcode in html or use `element.setAttribute(eventAttr, 'func()')` method
        ```js
        //1st
        const body = document.body;
        function handleClick() {
            console.log("body Clicked");
        }

        body.addEventListener("click", handleClick)
        //2nd
        const heading = document.querySelector('h1')
        heading.setAttribute('onclick', 'handleClick()')
        ```
    - event examples
        - click
        - change
- `example.com` webpage to check js code
- Importing script to html file
    - at the end of the body
    - `<script src=''></script>`
- Frameworks and libraries
    - Open-source, Proprietary
    - Libraries - reusable pieces of code with specific functionality
        - example - email address validation - a lot of specifications
    - Frameworks - provide structure to build with - blueprint
        - Framework interucts with developer's code
        - Django, spring, Exress, etc
        - Example - http request handling
    - Frameworks use a lot of libraries and your code
        - your code can also use some other libraries
    - Frameworks call you and contain libraries, you call libraries
    - Choose set of libraries
    - Faster development, fewer errors

### Module Summary
- HTML - create web pages
    - basic structure
    - semantic tags
    - form submittions - get, post method
        - validation
            - client-side, server-side
        - input type with validation
- CSS - look and layout of a document
    - adaptability (responsiveness)
    - layouts, grids, flexboxes(smaller)
    - units
    - selectors, pseudo-classes (state), pseudo-elements(specific part)
- JS
    - Interactivity
    - Variables and Basic Data Types
    - Operators
    - Functions
    - DOM manipulations
        - Selectors
        - Event handling
        - `document`
    - Scope
        - **const?**, var, let
- Libraries and frameworks
- [Additional Resources](https://www.coursera.org/learn/the-full-stack/supplement/Bs7qU/additional-resources)


## 3 WEEK: The full stack using Django
### Django architecture
- Django recap
    - Backend applictation and connect with Frontend application
    - project and apps
    - admin and structures
    - web frameworks
    - django-admin, manage.py
    - Advantages: Fast, feature-rich, security, scalability
    - MVT architecture
        - Model
            - migrations
            - queryset api
            - Form FormAPI, ModelForm
            - Admin panel, external mysql db
        - View
            - views and view logic
                - process, transform, retriee, render
            - handels request and returns responses
                - HTTPRequest object
                    - query string parameters
            - URLConf - routing
                - `urls.py`
                - namespacing
                - path parameters
            - Params
            - Methods
            - RegEx
            - Status codes and error handling
            - OOP and inheritance + generic views
        - Template
            - DTL
            - Template inheritance `include` `extends`
    - Debugging and testing
        - Error and bugs
        - Metrics
        - `DEBUG=True`
        - unit testing. `django.test` `TestCase`
- APIs recap
    - HTTP/HTTPS, client-server architecture
        - methods
        - http status codes for responses
    - RESTfulness
        - naming conventions
            - lowercase
            - `/` hierarchy
            - nouns
            - no file names
        - api development tools
    - Principles
        - REST best practices
        - security
        - authentication and authorization, access control
    - `Insomnia` rest client
    - Organization
        - xml, json response
        - structure
    - Debugging
        - vs code debugging tools
        - django debug toolbar
    - mock api - imitate real endpoints
        - test
        - develop
        - similar response
    - DRF - utility app for apis
        - create apis
        - serializers - convert into readable format
            - deserealization - parson json and map to a model
        - convert, validate, render
        - http status codes
        - routers - configure ulrs from class based views
        - Views
            - function
            - class based views
        - Renderer objects
        - filter, sort, pagination
            - querystring parameters
        - caching, performance
        - data sanitization
        - api security
            - token-based authentication
                - registration and login api
            - authorization - access control
                - user roles and permissions
            - `djoser` library
                - registration
        - api throttling: anon, user
- **Environment check**
    - Terminal
    - Django specific tools
        - pipenv - manage package dependencies + virtual env
    - DB
        - MySQL, MariaDB
        - install mysql
    - Editor - VScode + extensions
    - API testing - REST API client
        - Insomnia
        - Postman
        - `httpbin.org` service
    - VCS - Git, git bash
    - Front end tools
        - `Node.js` to work with react
            - had problems when installating.
        - `npm` or `yarn` package to deal with dependencies
        - build tool `Vite.jsor` or `Webpack` to build the production version of your code
            - Bundling
- Creating a django projects
    1. `mkdir project`
    2. `cd project`
    3. `django-admin startproject myproject .`
    4. `pipenv shell`
    5. Open pipfile and update it with
    ```
    [[source]]
    url = "https://pypi.org/simple"
    verify_ssl = true
    name = "pypi"
     
    [packages]
    django = "*"
    djangorestframework = "*"
    djangorestframework-xml = "*"
    mysqlclient = "*"
     
    [dev-packages]
     
    [requires]
    python_version = "3.9"
    ```
    6. `pipenv install` - will download dependencies from pipfile
        - or install `pipenv install:`
            - `django`, `djangorestframework` `djangorestframework-xml` `mysqlclient`
    7. `python3 manage.py startapp myapp`
    8. `python3 manage.py runserver`
- [Additional resources](https://www.coursera.org/learn/the-full-stack/supplement/bZ44Z/additional-resources)

- Questions
    - Why do we need nodejs, npm, webpack, vite.jsor and how to use it on basic level.

### Django and MySQL
- Databases and MySQL
    - Relational (PostgreSQL, MySQL), NonRelational
    - Keys, Constraints
    - Django
        - PostgreSQL, MariaDB, Oracle, **SQLite**, MariaDB
            - sqlite - prototyping and small projects
            - mysql - scalability, security(authentication)
        - settings
            - port, address, database
        - connection
    - MySQL
        - install mysql on local machine
            - `mysql -u root -p` - start mysql cli client
        - installing mysql db api driver
            - `mysqlclient` `pipenv install mysqlclient`
            - `CONN_MAX_AGE` - controlling connection with db
        - update mysql settings inside django project
        - **options** file to store a db connection **credentials**
            ```python
                'OPTIONS': {
                    'read_default_file': 'path' # dbname, host, user, password, default-character-set
                    # etc/mysql/my.cnf
                }
            ```
    - Connection and permissions
    - Security roles and security of credentials
- [Setting up a MySQL database on OS](https://www.coursera.org/learn/the-full-stack/supplement/Q0JjO/setting-up-a-mysql-database-on-windows)
- Models and Migrations
    - ORM
        - Model - python class `django.db.models.Model`
            - field - column in db
                - Formfield - datatypes
    - CRUD
        - create: create new object instance and `save` it
        - update: get object instance, change and save
        - delete: get object instance, delete it
    - `raw` functions
        - `Model.objects.raw(sqlstatement)`
    - table name = `app_model`
    - Relationships
        - One to One `OneToOne`
        - Many to Many `ManyToMany`
        - One to Many `ForeignKey`
    - Migrations
        - create and make change to db schema
        - migration files
            - dependencies and operations
        - `makemigrations` `migrate`
        - history
            - `show migrations`
            - `django migrations` table
- Configuring django to connect mysql
    1. Installing mysql 
    2. Installing `mysqlclient` api `pipenv install mysqlclient`
    3. Establish connection and create a database for a project
        - `mysql -u root -p`
        - `mysql -u root -P port -p` - specifying port
        - `mysql -u root -h host -p` - specifying host
    4. Configure django project database setting
        - db section
            - engine: mysql
            - name - db name
            - host
            - user - dont use root in the production
            - password
            - port - 3306 default
    5. Perform migrations
- Exercise: Connect Django to MySQL
- [Additional Resources](https://www.coursera.org/learn/the-full-stack/supplement/7IeDL/additional-resources)

- Questions
    - raw creation of relationship types between tables

### Django and The front end
- Forms and ModelForm
    - Forms needed to exchange data with users
    - 2 ways to make forms
        - using HTML, CSS, JS
        - using django `Form` api, templating, `ModelForm` class
            - `forms.py` file for forms
            - `django.forms`
            ```python
            class MyForm(forms.Form):
                first_name = forms.CharField(label="first name", max_length=100)
            ```
    - Creating a ModelForm and processing it
        1. Create a model
        2. Create a ModelForm and connect it to model
        ```python
        class MyModelForm(forms.ModelForm):
            class Meta:
                model = Model
                fields = '__all__'
        ```
        3. Create and configure a view to process form data
            - `form.is_valid`
            - `MyModelForm(request.POST)`
            - `form.save`
    - common Form datatypes
        - CharField, IntegerField, FloatField, FileField, EmailField, ChoiceField
- Fetching data using JS
    - 2 approaches to create an application
        - Client-side first
            1. Creating a front end application using HTML, CSS, JS, React, Templating, URL
            2. Define processing of requests and db interaction
        - Server-side first
            1. Building django API 
            2. Using supporting libraries to build forms
    - JS, AJAX, EventHandling
    - **JS Fetch API**
    - Example
        1. Configure project urls and db
        2. Create Model and ModelForm
        3. Create a view - rendering and processing data
            - Using `JsonResponse`  to fetch it via JS later
        ```python
        def form_view(request):
            form = MyModelForm()
            if request.method == "POST":
                form = MyModelForm(request.POST)
                if form.is_valid():
                    cd = form.cleaned_data()
                    mod = Model(
                        first_field = cd['first_field'],
                        ...
                    )
                    mod.save()
                    return JsonResponse({'message': 'success'})
            
            return render(request, template, {"form": form})
        ```
        4. Creating a template with a form and data fetching
        ```html
        ...
        <body>
            <form id='form' action='view endpoint' method='POST'>
                {% csrf_token %}
                {{ form.as_p }}
                <button type='submit' value='Send'>
            </form>
            <script>
                const form = document.getElementById('form')
                form.addEventListener('submit', submitHandler)
                function submitHandler(e) {
                    e.preventDefault()

                    fetch(form.action, {method: 'POST', body: new FormData(form)})
                    .then(response=>response.json)
                    .then(data=>{
                        if (data.message == 'success') {
                            alert("Successful")
                            form.reset()
                        }
                    })
                }
            </script>
        ```
    - What is fetch api and how to use it to create an application
- Querying APIs using JS
    - Fetch and send data to an API
    - Native
        - `XMLHttpRequest`
        - `fetch`
            - HTTP Methods
                - GET - make a call, convert response to json, process data\
                ```js
                fetch(endpoint)
                .then(response=>response.json)
                .then(data=>{
                    //processing logic
                    console.log(data)
                })
                ```
                - POST, PUT, PATCH
                    - `JSON.stringify()`
                    - `Accept` `Content` headers
                ```js
                fetch(endpoint, {
                    method: 'POST', // put patch the same, but endpoint contains id
                    headers: {
                        "Accept": 'application/json',
                        "Content-Type:" : 'application/json'
                    },
                    body: JSON.stringify(payloadDictObject)
                })
                .then(response=>response.json())
                .then(data => {
                    //processing logic
                })
                ```
                - DELETE
                ```js
                fetch(endpointWithID, {
                    method: "DELETE",
                    headers: {
                        "Accept": 'application/json',
                        "Content-Type:" : 'application/json'
                    }
                })
                .then(response=>response.json())
                .then(data => {
                    console.log(data)
                })
                ```
            - Token Authentication
                - `'Authentication' : 'Bearer ' + token` header to call
                ```js
                fetch(endpointWithID, {
                    method: "POST",
                    headers: {
                        "Accept": 'application/json',
                        "Content-Type:": 'application/json',
                        'Authentication': 'Bearer ' + token
                    },
                    body: JSON.stringify(payload)
                })
                .then(response=>response.json())
                .then(data => {
                    console.log(data)
                })
                ```
    - Third-party libraries (jQuery or **Axios**)
        - simpler interface because of wrapper around `XMLHttpRequest`

- Exercise: Submitting form with JS
    - Setting up a js event to submit form data as json object
    - display a successful form submittion alert using js
    - Create a form, model and template with js code using fetch to make call!

- Questions
    - Do I need to make redirect when processing a post request?
    - How to make AJAX calls using JS?
        - What is JS fetch api and how to use it properly?

### Module Summary
- Django recap
- API recap
- Environment check
- virtual, global, pipenv, mysqlclient, mysql connection
- DB and MySQL connection
- models and migrations recap
- Forms and ModelForms recap
    - model -> modelform -> configuring a view
- Fetching data using JS to process simple forms


- [Additional Resources](https://www.coursera.org/learn/the-full-stack/supplement/nuH7u/additional-resources)


## 4 WEEK: Production environment
### Web server environments
- Server and Serverless
    - Deployment process - uploading code to server
        - Manual - using FTP, SFTP, Rsync
        - Automated
            - developer make changes and pushes code
            - build tools receives a signal and create a build environment identical to production
                - runs tests
                - IF OK: build tools connect to server and upload code
            - `CI` - continuous integration - imitating development environment and run tests to ensure that everything is ok
            - `CD` - continuous deployment
            - CI/CD workflow
                - Code -> VCS -> Build -> Test -> Deploy
                - tools: `Jenkins` `CircleCI` `Github's CI`
                - no tests => only continuous deployment
    - Hosting - 2 approaches
        - Server - host companies
            - Dedicated
                - Full Access, Exclusive server, Add ram and storage
            - Virtual
                - Hypervisor software - dedicated server split into multiple virtual machines
                - configure with different OS, no conflict, different purposes
                    - db or application
        - Serverless
            - no configuration, storage, cpu, environment, memory allocation
            - everything managed by the serverless provider
            - starts working automatically
                - builds code, run tests, deploy code, provide access
                - bills by usage
                - locked to vendors environment
- Virtual machines and containers
    - Hypervisors - divide dedicated server into virtual ones with their own configuration, OS, and IP addresses
        - Type-1 - software layer that working directly with server hardware
            - faster, dedicated resources
            - `KVM` - open source
        - Type-2 - on top of the operating system
            - easier managing, slower
            - `Oracle virtual box` - open source
    - Resource sharing
        - Dedicated - availability, wastage
        - Shared - share resources from other machines when available
            - usage monitor, server termination, contiguous over-usage
    - Configure hypervisor and install os on virtual machine
    - Containerization - focus only on application and dependencies
        - pack your application and dependencies into container image files
        - Running as containers regardless of os and hardware
        - can pack single or multiple app with dependencies
        - Or use containers for each application and establish communication using a container engline (Docker)
        - Smaller, Faster, More Manageable
        - `Docker`
        - Terms
            - Pod - coupled containers, share a resource, work together
            - Cluster - multiple pods or nodes
            - Node - physical or virtual machine that runs on one or more pods
            - Managament, deployment, networking, scaling of this containers = Container Orchestration
                - `K8s` - Kubernetes
- Some other terminology
    - Cloud tools to host applications
        - self-hosted - do everything by yourself. When needed extra security. Expensive
        - IaaS - infrastructure as a service
            - offers infrastructural units on demand
                - load balancers, servers, vm, storage, computing units
            - AWS EC2, Google computing units, digital Ocean, Azure
        - PaaS - platform as a service
            - have essential tools to develop, build, host and run applications
            - focus more on business logic
            - AWS Elastic Beanstalk, Heroku, Cloudflare, Google app engine and Microsoft Azure, Facebook developer platform
        - SaaS - software as a service
            - application hosted on a cloud and allows to use it with an on-demand or pricing model
        - DBaaS - database as a service
            - db solutions
            - so you don't manually configure databases
- [Additional reading](https://www.coursera.org/learn/the-full-stack/supplement/72eRY/additional-resources)

### Introduction to cloud computing
- Cloud computing - on-demand solution that hosts application on the internet
    - Application takes a long time to run
        - Distribute to multiple computers
    - On-demand - specified amount on time
        - Latest CPU, GPU, massive memory and storage
    - Public Cloud - for everyone. host servers
        - more time creating and running application
        - quick availability, scalability, autoscaling, less expensive
        - automatically deploy extra nodes and remove them
    - Private cloud - more secure
        - Only authorized people can access the system
        - subset of features
        - Better security, control, scalability, reliability
    - Hybrid cloud - hosted on public and private cloud
        - complex setup, time sensitive
- Key elements of cloud computing
    - Computing units - virtual machines available for on-demand deployment
        - host web-application
        - 2 groups
            - Cores - resize
            - Memories
            - GPUs
        - Operating system and application
        - Volatile storage - permanent storage solution
    - Storage - purchase, keep your data, delete it
        - GBs, TBs - regular hard disk
        - backup
        - Object storage
            - upload, download files
            - available to everyone, timestamp signature
            - unique url
    - Databases
        - SQL (mysql, mariadb, postgresql)
        - NoSQL (mongodb, cassandra, dynamodb)
        - Time-series (influxdb, prometheu)
        - difficult, time-consuming, effortful - dissapear
        - Cloud
            - Managed solutions with MySQL, MariaDB, postgresql
                - scale automatically
                - Caching
    - BigData
    - Machine Learning
    - On-demand
    - More time on application development
- Networking in the cloud
    - Public vs private network
        - Accessed outside - public
        - private - accessed in the same network
    - IP Addresses
        - IPv4
            - private network addresses
        - IPv6
    - DNS system
        - DNS servers - store domain names against ip addresses
    - Bandwidth - data that comes in and out
    - Uplink network or com protocol to send data outside the server
        - downlink

### Scaling in the cloud
- What is scaling?
    - Resizing production infrustracture to withstand load changes
        - sudden
        - linear
    - Web server and DB server scaling
    - 2 types of scaling
        - vertical - quicker, easier configuration, has limitation, costly, repairs, not infinite. Add resources
        - horizontal - more efficient and cost effective
            - add nodes as the load goes up, and remove as goes down
            - database replication or clustering - multiple nodes
            - infinitely scalable
            - takes time and effort
    - fail reasons
        - Lack of resources - vertical. Cannot add infinite amount.
            - add more storage, ram, processing cores
            - upgrade
        - Incorrect configuration - Limited scaling
    - Autoscaling
        - Cloud provide automatically adds resources to keep an application sustainable
- Load balancer - evenly distributing load between nodes
    - web server
        - accepts http requests, processing, sending requests
        - static html, css, js files
        - Create multiple web servers with the same application code and connect them to the load balancer
        - 2 styles
            - round-robin - equally
                - not every request the same
            - health-based - monitor the load and distribute load accordingly
        - use `reverse-proxy` - serve static files and forward the application urls to web server
            - better performance, fewer requests
        - Offload static files to CDN
            - faster rendering, multiple copies
    - Database
        - more complex scaling
        - horizontal better
            - 2 techniques
                - Sharding - large database is split in multiple chunks
                    - one db holds one chuck
                    - one extra db needed to keep track of chunks
                - Master-slave replication
                    - multiple servers with the same db
                    - master server
                    - changes written on slave servers
                    - read requests distributed to the slave servers
    - Managing in the cloud
- How a CDN improves scaling?
    - CDN holds static files and deliver to user from the nearest server
        - Faster
        - Less direct traffic to your application
- Questions
    - What is reverse-proxy?

### Module Summary
Production environments
- Webserver environments
    - Deployment
        - CI - tests
        - CD - uploading process
    - Server or Serverless
    - VM and contarization
        - Type-1
        - Type-2
    - Resource sharing
- Containerization
    - Pod - group of containers with same resource
    - Node - multiple pods
    - Container orchestration
- PaaS, SaaS, DBaaS, IaaS, Self-Hosted
- Cloud computing - vm on-demand deployment
    - Public
    - Private
    - Hybrid
- Storage
- Machine Learning
- Networking in the cloud
- Scaling in the cloud
    - Vertical - add resources
    - Horizontal - configuration, nodes, virtual servers
    - Auto-scaling
- Load balancing
    - Round robin
    - Health based
    - Reverse proxy
- CDN - caching static asseets


## 5 WEEK: Final project
- Course Recap
    0. Connect to mysql, setting api, create app displaying available booking times
    1. Full Stack
        - everything to create and deliver a functioning application
        - DevOps Skills
        - VCS
        - N-tier architecture (Security, Scalability, Maintanence)
        - Client-server architecture
    2. Front-end technologies
        - HTML - form, input types validation
        - CSS - layouts, grids, flexboxes, selectors, pseudo-classes and elements
        - JS - interactivity, DOM manipulation, datatypes, event handling, Libraries and frameworks
    3. Recap
        - Django, APIs, DB, Tools, DRF
        - JS Fetch api
    4. Production environments
        - Web server environments and deployment
        - CI/CD (tests and uploading)
        - Server and Serverless
        - VM: Type-1 type-2
        - Containerization
        - PaaS, IaaS, SaaS, DBaaS etc
        - Cloud infrustructure
            - computing unit
            - storage options
            - Netwroking ,scaling, load balancing
        - CDNs
- Final Assignment
    - Exercises
        - connect to mysql
        - setup a little lemon api
            - create a view to process form data entered
        - display booking
    - Essentials
        - Creating an new user for mysql db.



# Course Syllabus (SIR)
1. Introduction to the fullstack
    - N-tier architecture
    - Client-server architecture
2. Front-end technologies
    - HTML
        - Tags and semantic tags
        - Form validation and submittion
            - input types
    - CSS
        - Web Layout
        - Selectors
        - Document flow, grids, flexbox, inline, block
        - Pseudo-classes and pseudo-elements
    - JS
        - Variables, var, let, const
        - datatypes, operators
        - Selectors
        - Functions
        - DOM manipulations
        - Event handling
        - Framework and libraries
3. The full-stack with Django
    - Django architecture
    - Django and MySQL db
    - Django and Frontend