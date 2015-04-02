"""
Django settings for freedomvote project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import ConfigParser
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEFAULT_SETTINGS = {
    'DB'           : {
        'NAME'     : 'freedomvote',
        'USER'     : 'freedomvote',
        'PASS'     : 'vagrant',
    },
    'GLOBAL'       : {
        'DEBUG'    : 'True',
        'BASE_URL' : 'http://freedomvote.vm',
    },
    'PIWIK'        : {
        'SITE_ID'  : 0,
        'URL'      : '',
    }
}

try:
    config = ConfigParser.ConfigParser()
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
SECRET_KEY = '%xky6n0ak0m*97&3o=zd45_w7o(q(1)o^54y(6)c34rl1u4m^_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEFAULT_SETTINGS['GLOBAL']['DEBUG'].lower() == 'true'
THUMBNAIL_DEBUG = True
TEMPLATE_DEBUG = True
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
    'debug_toolbar',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'djangocms_text_ckeditor',
    'easy_thumbnails',
    'django_js_reverse',
    'core',
    'modeltranslation',
    'django.contrib.admin',
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'djangocms_admin_style',
    'django.contrib.messages',
    'piwik',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
)

MIGRATION_MODULES = {
    'cms'                     : 'cms.migrations_django',
    'menus'                   : 'menus.migrations_django',
    'djangocms_text_ckeditor' : 'djangocms_text_ckeditor.migrations_django'
}

ROOT_URLCONF = 'freedomvote.urls'

WSGI_APPLICATION = 'freedomvote.wsgi.application'

INTERNAL_IPS = [
    '0.0.0.0',
    '127.0.0.1',
]

TEMPLATE_DIRS = (
    # The docs say it should be absolute path: BASE_DIR is precisely one.
    # Life is wonderful!
    os.path.join(BASE_DIR, "templates"),
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':     DEFAULT_SETTINGS['DB']['NAME'],
        'USER':     DEFAULT_SETTINGS['DB']['USER'],
        'PASSWORD': DEFAULT_SETTINGS['DB']['PASS'],
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'de'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'de'

LANGUAGES = (
    ('de', _('german')),
    ('fr', _('french')),
    ('it', _('italian')),
)

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
        'medium' : {'size' : (300, 300), 'crop' : True, 'quality' : 100},
        'small'  : {'size' : (120, 120), 'crop' : True, 'quality' : 100},
        'large'  : {'size' : (500, 500), 'crop' : True, 'quality' : 100},
        'icon'   : {'size' : ( 16,  16),   'crop' : True, 'quality' : 100},
    },
}

PIWIK_SITE_ID = DEFAULT_SETTINGS['PIWIK']['SITE_ID']
PIWIK_URL = DEFAULT_SETTINGS['PIWIK']['URL']
