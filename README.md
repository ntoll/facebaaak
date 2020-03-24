# Simple Django

A simple example Django project for tutorial purposes.

## Setup

Open up your terminal.

Clone the repository:

```
git clone git@github.com:ntoll/simple_django.git
```

Create a virtualenv:

```
python3 -m venv my_venv
```

Activate it on unix-y OS's:

```
source my_venv/bin/activate
```

Activate it on Windows:

```
my_venv\Scripts\activate
```

Change into the directory for the simple django website and install all the
dependencies.

```
pip install -r requirements.txt
```

(You may need to upgrade `pip`):

```
pip install --upgrade pip
```

Setup the local Sqlite database:

```
python manage.py migrate
```

Run the local development server:

```
python manage.py runserver
```

You should be able to visit the website at: http://127.0.0.1:8000/
