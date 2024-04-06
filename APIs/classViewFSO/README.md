# Description

Fast CRUD project with:
1. filtering seraching and ordering
2. Throttling

## Steps Filtering
0. pipenv install django - creating virtualenv for project
pipenv shell
pipenv install 
    - djangorestframework
    - debug
        - django-debug-toolbar
    - renderers
        - djangorestframework-csv
        - djangorestframework-yaml
        - djangorestframework-xml
1. Creating project
2. Creating APP - adding to settings
3. Creating models - migrations
4. Creating viewsetbased class
    - creating serializers
    - creating views
    - Mapping urls
5. Configuring REST_FRAMEWORK setting for renderers, filtering, ordering, searching, pagination
5. Configuring debug toolbar

# Steps Throttling
0. Create authentication by token system
1. Create a view
2. use `throttle_classes` field or use `get_throttles` method
3. Configure throttle rates at settings `DEFAULT_THROTTLE_RATES: (name: rate)` and `DEFAULT_THROTTLE_CLASSES`
4. For custom in `throttles.py` create subclass of throttle class with `scope` field as a name