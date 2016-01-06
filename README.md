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

Configure your DB settings in `app/freedomvote/settings.py` and then run:
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

# Languages
The whole application is multilingual. Per default the languages German, Italian and French are installed.
The translation are located in `app/locale/<lang_code>/LC_MESSAGES/django.po`. After editing the translation, run `python manage.py compilemessages`

To install another language (English in this example) make the following steps:

app/freedomvote/settings.py

```python
LANGUAGES = (
  ...
  ...
  ('en', _('english')),
)
```

in your environment:

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
