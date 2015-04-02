# Freedomvote
A django politician portal app
# Installation
## Requirements
* python >= 2.7
* django >= 1.7
* django-debug-toolbar >= 1.3
* django-modeltranslation >= 0.8
* pillow >= 2.7
* psycopg2 >= 2.4.5
* easy-thumbnails >= 2.2
* django-cms >= 3.0.12
* django-js-reverse >= 0.4.5
* djangocms_text_ckeditor >= 2.4.3
* django-piwik>=0.1
* libjpeg
* zlib

## Vagrant
To run Freedomvote in a VM, you need to install vagrant and virtualbox and execute those commands:
```
$ make vagrant                   # build vagrant box
$ make vagrant-collectstatic-dev # collect all staticfiles
$ sudo make domains              # add subdomains to /etc/hosts
$ make vagrant-runserver         # run development server
```
Now you can access the frontend on http://freedomvote.vm/admin/ and PhpPgAdmin on http://db.freedomvote.vm/

## Languages
The whole application is multilingual. Per default the languages German, Italian and French are installed.
The translation are located in app/locale/\<LANG_CODE\>/LC_MESSAGES/django.po. After editing the translation, run `python manage.py compilemessages`

To install another language (English in this example) make the following steps:

app/freedomvote/settings.py
```
LANGUAGES = (
  ...
  ...
  ('en', _('english')),
)
```
in your environment:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py makemessages -l en
$ python manage.py compilemessages
```

# License
GPLv3 see [LICENSE](https://github.com/adfinis-sygroup/freedomvote/blob/master/LICENSE)
