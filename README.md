neo4django-tutorial
===================

The django tutorial, backed by neo4django. This follows along with the official
Django [tutorial](https://docs.djangoproject.com/en/1.4/intro/tutorial01/).
Also see this [documentation for the neo4django
module](https://neo4django.readthedocs.org/en/latest/index.html).

# Installation steps

Clone this repository and `cd` into it.

## Install Django and neo4django

    pip install -r requirements.txt

## Install Neo4j

    source setup_env_neo4j.bash

This script downloads and installs Neo4j 1.8.1 locally in the current
directory. It then starts Neo4j running. To stop Neo4j, invoke the command

    neo4j stop

from the command line.

# Create the Django project

    django-admin.py startproject mysite

Test it by running the development server and opening the URL to the homepage.

    python manage.py runserver

## Set up the databases

*(These source code editing steps have already been done in this repository.)*

Edit `mysite/settings.py`:

```python
import os

# ...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'test_database.sqlite3')
    }
}

NEO4J_DATABASES = {
    'default' : {
        'HOST':'localhost',
        'PORT':7474,
        'ENDPOINT':'/db/data'
    }
}
```

Create the tables in the Sqlite3 database.

    python manage.py syncdb

# Create an app

    cd mysite
    python manage.py startapp polls

Edit `polls/models.py` to contain this:

```python
from neo4django.db import models

class Poll(models.NodeModel):
    question = models.StringProperty(max_length=200)
    pub_date = models.DateTimeProperty('date published')

class Choice(models.NodeModel):
    poll = models.Relationship(Poll,
                               rel_type='offers',
                               single=True,
                               related_name='choices')
    choice = models.StringProperty(max_length=200)
    votes = models.IntegerProperty()
```

Add `polls` to the list of installed apps in `mysite/settings.py`:

```python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    polls,
)
```

## Playing with the API

We can start the interactive Python shell and play around with the API. To
invoke the Python shell, use this command:

    python manage.py shell

The neo4django documentation provides some
[examples](https://neo4django.readthedocs.org/en/latest/writing-models.html) of
using the API.

*This concludes part 1 of the tutorial.*
