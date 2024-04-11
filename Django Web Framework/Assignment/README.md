# Assignments
Format
week: title
description, questions, some needed theory
**Sequence of steps for labs**

## 1: Creating your first project and app


## 1: Module Quiz


## 2: Creating a view and URL configuration

## 2: Mapping URLs with Params

## 2: Creating URLs and Mapping to Views

## 2: Module Quiz: Views


## 3: Models and Migrations

## 3: Models using Foreign Keys


## 3: Working with forms

## 3: Using Django Admin


## 3: Database configuration


## 3: Module Quiz: Models


## 4: Creating Templates

## 4: Creating Dynamic Templates

## 4: Working with Templates

## 4: Module Quiz


## 5: Design and build a simple Django app
Little Lemon Django project
Home, About, Book pages are completed

#### Little Lemon Website
5 pages
- Home
- About
- Booking
- Menu
- Menu Item
Project contains static files.

#### Task:
1. Create menu page
    1. Define `Menu` (name charf 200, price int) models with `__str__` methods
        - register to admin panel
        - migrations
    2. Check app and project level `urls.py` for existing pages
    3. Populate menu
        - Create super user (bistroadmin, admin@littlelemon.com, lemon@786!)
        - run server, go to admin page, populate [the menu](Menu.md)
    4. Views
        - create menu view
            - menu_data - get data from model
            - main_data - dictionary for the content of the template
            - render
        - map the view to corresponding url
    5. Template
        - Create menu.html [template](menu.html)
        - Modify template
2. Create menu item page
    1. Update menu model - description text max=1000 def=''
        - update descriptions in admin
    2. View display_menu_items(req, pk=None)
        - menu_item variable if else
        - render template
        - map url
    3. menu_item.html template and menu.html template
        - add links to menu items on `menu`
        - Modify templates
3. Create footer
    - _footer.html


Static tag takes only variable or string.
[Solution Code](https://www.coursera.org/learn/django-web-framework/supplement/duTb2/solution-code)

## 5: Peer review rubric: Design and Build a simple Django app
- Criterias
- Zip project and upload
- Peer review 3 projects

## 5: Final quiz