# Freedomvote
A tool to represent the views of politicans as a help to the voters.
![freedomvote.ch](https://raw.githubusercontent.com/adfinis-sygroup/freedomvote/master/tools/screenshot.png)
# Installation
## The "hard" way
Requirements:

* python 2.7
* postgresql
* python-pip

Run `pip install -r requirements.txt` to install all requirements.

Configure your DB settings in `app/settings.ini`:

```ini
[DB]
NAME = freedomvote
USER = freedomvote
PASS = ***********
PORT = 5432
HOST = 127.0.0.1
```

and then run:

```bash
$ psql -h <db_host> -U <db_user> <db_name> < tools/docker/cache_table.sql
$ python app/manage.py migrate
$ python app/manage.py createsuperuser
$ python app/manage.py runserver
```

Now you can access the frontend on http://localhost:8000

## The easy way - Docker
To run Freedomvote in a docker container, you need to install docker and docker-compose and execute those commands:

```bash
$ make docker-init docker
```
Default user is `admin` with password `123qwe`, to change this, run `make docker-pw`

Now you can access the frontend on http://localhost:8000

## Django management
Django already provides a number of [management commands](https://docs.djangoproject.com/en/1.10/ref/django-admin/) out of the box.
Other parts of this document already lists the usages of some of these commands.
Freedomvote provides a couple of custom commands to ease the setup process:

```bash
$ python app/manage.py help
$ python app/manage.py help <command>
$ python app/manage.py generate_politicians 42
$ python app/manage.py politician_import politician_import.csv.example
$ python app/manage.py user_import user_import.csv.example
```
## LinkType icons
In the management dashboard custom LinkTypes can be configured with both name and icon.
A fixture is included with this repository to help you configure a common set of link types easily.
Note that if some of these LinkTypes already exist, triggering this command will add the new ones regardless of existing LinkTypes.

`$ python app/manage.py loaddata fixtures/linktypes.json`

This common set of icon was gathered from [fontawesome](http://fontawesome.org/) using [icon_font_to_png](https://pypi.python.org/pypi/icon_font_to_png/0.3.2).

# Languages
The whole application is multilingual. Per default the languages German, Italian and French are installed.
The translation are located in `app/locale/<lang_code>/LC_MESSAGES/django.po`. After editing the translation, run `python manage.py compilemessages`

To install another language (English in this example) make the following steps:

`app/freedomvote/settings.py`
```python
LANGUAGES = (
  ...
  ...
  ('en', _('english')),
)
```
then create a new folder for the language:
```bash
$ mkdir app/locale/en
```
now run those commands in your environment:
```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py makemessages
$ python manage.py compilemessages
```
or with docker:
```bash
$ make docker-makemigrations
$ make docker-migrate
$ make docker-makemessages
$ make docker-compilemessages
```

# License
GPLv3 see [LICENSE](https://github.com/adfinis-sygroup/freedomvote/blob/master/LICENSE)
