

## 1: Module Quiz

## 2 Creating a grid layout
```css
.container {
    /* Add rules here */
    display: grid;
    max-width: 900px;
    min-height: 50vh;
    grid-template-columns: 100%;
    grid-template-rows: auto auto 1fr auto auto;
    grid-template-areas: "header" "left" "main" "right" "footer";
}
/* Add media rules for container class below */
@media (min-width: 440px) {
    .container {
    /* Add rules here */
      grid-template-columns: 150px 1fr 150px;
      grid-template-rows: auto 1fr auto;
      grid-template-areas: "header header header"
                           "left main right"
                           "footer footer footer";
    }
}
/* grid area property to define area of grids */
```


## 2: Exercise: Declaring variables


## 2: Exercsise: Web page content update
- `prompt` function to take user input and then manipulate DOM to display it.
dynamically create a page
```js
var h1 = document.createElement('h1')
h1.innerText = "Type into the input to make this text change"

var input = document.createElement('input')
input.setAttribute('type', 'text')

document.body.innerText = '';
document.body.appendChild(h1);
document.body.appendChild(input);

input.addEventListener('change', function() {
    h1.innerText = input.value
})
```


## 2: Module Quiz


## 3: Connect Django to MySQL

## 3: Submitting a form with JS
- Download the project zip file
- Unpacking and creating virtual env, installing dependencies
1. creating a db from settings
2. Checking modesl and forms
3. pipenv shell pipenv install
4. migrations
5. Creating view
6. Fill template (from decsription)
7. Add script tag at the end and write code in js
    - Submittion of form and fetch function.
8. Runserver and create several entities


## 3: Module Quiz

## 4: Module Quiz


## 5: Final Project
Ex1 - Mysql
0. Some assets given by the course.
1. Connect to mysql via cmd and create a db reservations
2. run pipenv and install dependencies
3. **Create a new user for the database and Grant him permissions. Flush privileges.**
    - admindjango employee@123!
4. Add myapp to the project and configure db settings. Check booking 
5. Migrations
6. show tables; use db; describe table ect.

Ex2 - booking api
0. Assets and code given by the course
1. Run pipenv shell and install django and mysqlclient
2. create forms.py in restaurant app -> import booking model and forms
    - Create BookingForm as ModelForm
    - Meta in BookingForm with model=Booking, fields all
3. Perform migrations
4. Go to views.py
    - remove comments for book view and imports
    - create new function booking() with pseudocode from decsription
5. configure routes
6. Open book.html
    - modify script and html
7. Open booking.html
    - same
8. Open index.html
    - same
9. Test app


Ex3 - display available booking times
0. Load code zip
1. pipenv shell and install django and mysqlclient
2. perform migrations, check db config
3. views.py
    - create bookings() below the @csrf_exempt decorator
        - code from description
4. Book.html
    - Code from description


## 5: Reviews
```shell
cd <project directory>

pipenv shell

pipenv install 

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

## 5: Final quiz