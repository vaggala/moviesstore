chapter 1:
- django is a web framework used to make apps in python
- similar to sb for java
- running examples are 
    - tools used to demonstrate methodologies, processes, tools, techniques of a specific app and its internal workings
- Django is MVT architecture style (Model View Template)
    - ios club is MVVM (Model View View-Model)
    - models r the python classes that define data and how it interacts in a db.
        - they handle CRUD tasks 
        - movie, review, order, user, item are all models
    - views r how the app process requests from a backend perspective
    - temgplates are how the app looks to the users after processing requests (i.e cart get updated w/ movie after adding to cart)
- ```python3 manage.py runserver```

Chapter 2:
- django app is self contained package of code
- can have multiple apps, such as one for user auth, one for listing payments, etc.
- these work tg to make the overall application run smoothly
- Creating a simple page or section in Django usually involves three steps:
    - Configure a URL.
    - Define a view function or class.
    - Create a template.
- for this project, to create urls, we will define at the app level
    - eg. home/url.py instead of moviesstore/url.py
- suggested to store your app templates under the next directory structure – app_name/templates/app_name/my_template.html.
    - e.g. home/templates/home/index.html
