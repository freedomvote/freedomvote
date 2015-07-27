# Freedomvote
A django politician portal app
# Installation
## Requirements
* python >= 2.7
* python-pip

Run `pip install -r requirements.txt` to install all requirements.

## Docker
To run Freedomvote in a docker container, you need to install docker and docker-compose and execute those commands:

```bash
$ make docker-init docker
```

Now you can access the frontend on http://localhost:8000

## Languages
The whole application is multilingual. Per default the languages German, Italian and French are installed.
The translation are located in app/locale/\<LANG_CODE\>/LC_MESSAGES/django.po. After editing the translation, run `python manage.py compilemessages`

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
$ python manage.py makemessages -l en
$ python manage.py compilemessages
```

# License
GPLv3 see [LICENSE](https://github.com/adfinis-sygroup/freedomvote/blob/master/LICENSE)
