#!/usr/bin/env python3
"""
Django settings for freedomvote project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import configparser
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEFAULT_SETTINGS = {
    'DB'                   : {
        'HOST'             : 'db',
        'NAME'             : 'freedomvote',
        'USER'             : 'freedomvote',
        'PASS'             : 'freedomvote',
        'PORT'             : '5432',
    },
    'GLOBAL'               : {
        'DEBUG'            : 'True',
        'BASE_URL'         : 'http://localhost:8000',
        'DEFAULT_LANGUAGE' : 'en',
        'LANGUAGES'        : 'de,en,fr,it,nl',
        'SECRET'           : 'someverysecretrandomkey'
    },
    'PIWIK'                : {
        'SITE_ID'          : 0,
        'URL'              : '',
    },
    'EMAIL'                : {
        'BACKEND'          : 'django.core.mail.backends.smtp.EmailBackend',
        'HOST'             : 'localhost',
        'HOST_USER'        : '',
        'HOST_PASSWORD'    : '',
        'PORT'             : '25',
        'USE_TLS'          : 'False',
        'USE_SSL'          : 'False',
        'FROM'             : 'webmaster@localhost'
    }
}

try:
    config = configparser.ConfigParser()
    config.readfp(open(os.path.join(BASE_DIR, 'settings.ini')))

    for key in config._sections:
        DEFAULT_SETTINGS[key].update({
                k.upper():v
                for k,v
                in config.items(key)
        })

except:
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Thanks to Sander Bos for reporting the security issue
SECRET_KEY = DEFAULT_SETTINGS['GLOBAL']['SECRET']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEFAULT_SETTINGS['GLOBAL']['DEBUG'].lower() == 'true'
THUMBNAIL_DEBUG = True
SITE_ID = 1
DEBUG_TOOLBAR_PATCH_SETTINGS = False

ALLOWED_HOSTS = ['*']

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

BASE_URL = DEFAULT_SETTINGS['GLOBAL']['BASE_URL']

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL  = '/media/'

# Application definition

INSTALLED_APPS = (
    'modeltranslation',
    'colorfield',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.admin',
    'django.contrib.messages',
    'treebeard',
    'menus',
    'sekizai',
    'easy_thumbnails',
    'piwik',
    'core',
    'api',
    'cms',
    'meta',
    'rest_framework',
    'django_filters'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [ os.path.join(BASE_DIR, "templates") ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors':
                (
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                )
        }
    },
]

ROOT_URLCONF = 'freedomvote.urls'

WSGI_APPLICATION = 'freedomvote.wsgi.application'

INTERNAL_IPS = [
    '0.0.0.0',
    '127.0.0.1',
]

## Has to be allocated to an empty array to show the toolbar on /?edit because of the update of django cms
CMS_INTERNAL_IPS = []

CMS_PLACEHOLDER_CACHE = False
CMS_PAGE_CACHE = False
CMS_PLUGIN_CACHE = False
CMS_CACHE_DURATION = 0

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#        'LOCATION': 'cache_table',
#    }
#}

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     DEFAULT_SETTINGS['DB']['NAME'],
        'USER':     DEFAULT_SETTINGS['DB']['USER'],
        'PASSWORD': DEFAULT_SETTINGS['DB']['PASS'],
        'HOST':     DEFAULT_SETTINGS['DB']['HOST'],
        'PORT':     DEFAULT_SETTINGS['DB']['PORT'],
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = DEFAULT_SETTINGS['GLOBAL']['DEFAULT_LANGUAGE']

MODELTRANSLATION_DEFAULT_LANGUAGE = DEFAULT_SETTINGS['GLOBAL']['DEFAULT_LANGUAGE']

LANGUAGES = [
    lang for
    lang in [
        ('de', _('german')),
        ('en', _('english')),
        ('fr', _('french')),
        ('it', _('italian')),
        ('nl', _('dutch'))
    ]
    if lang[0] in DEFAULT_SETTINGS['GLOBAL']['LANGUAGES'].split(',')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CMS_TEMPLATES = (
    ('home.html', 'Home'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

THUMBNAIL_ALIASES = {
    '': {
        'small'  : {'size' : (50,   50), 'crop' : True, 'quality' : 100},
        'medium' : {'size' : (300, 300), 'crop' : True, 'quality' : 100},
        'large'  : {'size' : (500, 500), 'crop' : True, 'quality' : 100},
        'icon'   : {'size' : ( 16,  16), 'crop' : True, 'quality' : 100},
    },
}

PIWIK_SITE_ID = DEFAULT_SETTINGS['PIWIK']['SITE_ID']
PIWIK_URL = DEFAULT_SETTINGS['PIWIK']['URL']

GIT_URL = 'https://github.com/freedomvote/freedomvote'

# Metadata settings (according to https://django-meta.readthedocs.io/en/latest/settings.html)
META_SITE_PROTOCOL = BASE_URL.split('://')[0] or 'http'
META_SITE_DOMAIN = BASE_URL.split('://')[1] or 'localhost:8000'
META_SITE_TYPE = 'website'
META_DEFAULT_KEYWORDS = ['freedomvote', 'elections', 'politicians', 'states']
META_INCLUDE_KEYWORDS = META_DEFAULT_KEYWORDS
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True
META_OG_NAMESPACES = True

EMAIL_BACKEND = DEFAULT_SETTINGS['EMAIL']['BACKEND']
EMAIL_HOST = DEFAULT_SETTINGS['EMAIL']['HOST']
EMAIL_HOST_USER = DEFAULT_SETTINGS['EMAIL']['HOST_USER']
EMAIL_HOST_PASSWORD = DEFAULT_SETTINGS['EMAIL']['HOST_PASSWORD']
EMAIL_PORT = DEFAULT_SETTINGS['EMAIL']['PORT']
EMAIL_USE_TLS = DEFAULT_SETTINGS['EMAIL']['USE_TLS'].lower() == 'true'
EMAIL_USE_SSL = DEFAULT_SETTINGS['EMAIL']['USE_SSL'].lower() == 'true'
DEFAULT_FROM_EMAIL = DEFAULT_SETTINGS['EMAIL']['FROM']
