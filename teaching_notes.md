# Django Core Concepts

## Technical setup:

* Check screen share.
* Folks should have a code editor.
* git clone https://github.com/ntoll/facebaaak.git
* Follow setup instructions.

## Concepts:

* A website contains "apps"
* An app has models, views, forms, signals, urls, templates and tests.
* Models define the data layer.
* Forms define web-forms and manage the validation and cleaning of user input.
* Templates define how to render the HTML to be returned to the user.
* Signals allow decoupled message passing. Certain actions emit signals, others receive (and process) them.
* Urls define how program logic (in views) is related to the paths available to users.
* Views contain application logic expressed as functions or classes.
* tests - unit tests.

Django has many apps. We'll be using five:

* Crispy forms - helps us to control the rendering of forms.
* Gravatar - for user avatars.
* Markdown - for rendering user generated textual content.
* Django Rest Framework - for quickly creating a RESTful API to complement our website.
* YASG - yet another swagger generator.

Django is:
    
* Full stack
* Opinionated
* Well integrated
* Well supported
* Has an active and vibrant community.
* Probably has what you're looking for already.

Django is a good way to learn Python.

Contrast with flask:

* Minimal
* Scaffolding
* Provides core request handling
* You choose other libraries for handling other things

Introduce Facebaaak:

* A very simple website.
* Comes with its own API.
* A fun way to encounter many core Django concepts.


## Models:

* Explain ORM / Relational data.
* Look at users.models for profile and follows classes.
* Look at bleet.models.
* Comments therein make it clear how it works.

A practical example of using Django's ORM layer to interact with the database.

Start the Django shell:

```
    $ ./manage.py shell
```

Then, within the shell:

```
from django.contrib.auth.models import User
from bleet.models import Bleet
from users.models import Profile, Follow
u = User.objects.get(username="ntoll")  # returns a single result or None
dir(u)
u.password
u.email
u.profile
u.profile.bio
u.profile.bio = "Some new bio"
u.save()
results = User.objects.filter(email="ntoll@ntoll.org")  # returns a result set. Lazy!
```

Discuss database backends: Postgres, Sqlite, Mysql etc...

## Forms:

* Closely linked to the metadata created in the model layer.
* Can be generated manually, but Django does safe things by default.
* All forms both validate user entry and *clean* user entry.
* Django comes with many existing common forms (django.contrib)
* Look at users.forms
* Comes with very powerful form validation process (https://docs.djangoproject.com/en/3.0/ref/forms/validation/)


## Templates:

* Contain fragments of the HTML to be rendered to the user.
* Are rendered within a context (containing data from the models layer, and forms).
* The context is assembled in the view layer (see later)
* Forms includes a very powerful templating language which allows templates to extend parents, re-use snippets for common UI elements.
* Conditionals, loops and plug-ins are available.
* Define aspects of the templates via blocks which are overridden in child templates.
* `{% thing %}` for logic... `{{ thing }}` to render a value.
* Look at the various templates in bleet and users.


## Signals:

* Signals are emitted in various aspects of the application (for example when models are created).
* Used to "signal" something has happened. Receivers are registered to process such signals.
* A good example in users.signals
* Describe decorators

## Urls:

* There is a base urls.py which is used as a "traffic policeman" to point routes to the correct view.
* Apps can also have urls (which are referenced in the base urls.py). These define how such sub-endpoints should behave in the app.
* Look at the urls. Modern way to do things is via "path", but you may see "urls" in docs.

## Views:

* Come in two sorts: as functions called with a request and matched values from the urls pattern.
* As a class which is instantiated with references to the request. Each view class inherits mixins which provide constraints and capabilities (see LoginRequiredMixin in bleets.views).
* In a class view the life-cycle of the request is fulfilled by calling various methods in the required order. Various aspects of the view (such as the template to render) are set as attributes to the class.
* I prefer function based views (old skool) for simple request handling, but class based views (brave new world) for common CRUD activities. See users.views and bleets.views for examples.

## Settings:

* Configure once - usually here. See Django docs for scope and side effects of important settings.
* INSTALLED_APPS
* Database configuration
* REST_FRAMEWORK - authenticator classes - token based..!

## Adding an API layer:

* Serializers define the API representation (as JSON, XML etc). Clean the data and act as a broker with the outside world.
* ViewSets define the view behaviour. Mostly standard CRUD operations with the ability to override default behaviour or make things bespoke. ViewSets are associated with a Serializer.
* Routers provide an easy way of automatically determining the URL configuration (semantic URLs) and how they relate to the ViewSets that handle them.

## Documenting the API.

* Swagger docs via drf_yasg (django rest framework: yet another swagger generator).
* See urls.py for schema view generation with default values for various important settings.
* Add to the urlpatterns and swagger does the rest via code introspection.
