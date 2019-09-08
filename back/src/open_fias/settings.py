"""
Django settings for open_fias project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a8=z!w8^&&118)4fly@fjr6=$%$6dp25+n+_@!orfte)v1tyq7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

# TODO удалить ненужные хедеры

INTERNAL_IPS = ('127.0.0.1',)

ALLOWED_HOSTS = [
    '172.17.0.1',
    'localhost',
    '172.20.10.2',
    '172.20.10.4',
    'localhost',
    'localhost:3000',
    '192.168.1.38:3000',
    '89.208.86.148',
]

CORS_ORIGIN_WHITELIST = (
    'localhost',
    'localhost:3000',
    '172.20.10.2',
    '172.20.10.4',
    '172.20.0.1',
    '89.208.86.148',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'Cache-Control',
    'Cookie',
    'accept',
    'Access-Control-Allow-Origin',
    'Access-Control-Allow-Credentials',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

CSRF_TRUSTED_ORIGINS = (
    'localhost:3000',
    '172.20.10.2',
    '89.208.86.148',
)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'maps.apps.MapsConfig',
    'social_django',
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'open_fias.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'open_fias.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '',
    }
}

AUTH_USER_MODEL = 'users.User'

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'fias-memcached:11211'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

AUTHENTICATION_BACKENDS = (
    'social_core.backends.openstreetmap.OpenStreetMapOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# SOCIAL_AUTH_OPENSTREETMAP_KEY = '1CSi8bF1rfhygalXDPkqv5oRbXWYka7SneEZftM8'
# SOCIAL_AUTH_OPENSTREETMAP_SECRET = 'g2PrB2LIFXOwcoB3zCuZVsx4NzFYyqyS0apIMcG9'
SOCIAL_AUTH_OPENSTREETMAP_KEY = 'L2A3cFQqUUA5vDuzs0GvI8FpIvYNiZzqf5nhTQnC'
SOCIAL_AUTH_OPENSTREETMAP_SECRET = 'jzTDYR7tOM4KSR2FwYmfV29gWQMiIpzaEZxoxajZ'
SOCIAL_AUTH_OPENSTREETMAP_SCOPE = ['email', 'username', 'login', 'name']

# OPENFIAS_FRONTEND = 'http://89.208.86.148/'
OPENFIAS_FRONTEND = 'http://localhost/'

LOGIN_URL = OPENFIAS_FRONTEND
LOGIN_REDIRECT_URL = OPENFIAS_FRONTEND
LOGOUT_REDIRECT_URL = OPENFIAS_FRONTEND

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TESTING = 'test' in sys.argv
if TESTING:
    USE_TZ = False
    # DATABASES['default'] = {'ENGINE': 'django.db.backends.postgresql_psycopg2'}

# Centrifuge

CENTRIFUGE_URL = 'http://fias-centrifugo:9000'
CENTRIFUGE_SECRET = os.environ.get('CENT_SECRET')
CENTRIFUGE_APIKEY = os.environ.get('CENT_API_KEY')
CENTRIFUGE_TIMEOUT = 10

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Settings for FIAS

FIAS_API_KEY = 'None'
FIAS_URL_SUGGEST = 'v2/suggest/fias'
FIAS_URL_GEOCODER = 'v1/search'
FIAS_URL_REV_GEOCODER = 'v1/address'
FIAS_URL = 'http://geocode.maps.me'
# FIAS_URL = 'http://geocode.mapsme.devmail.ru'

OSM_URL_OBJECT_CREATE = 'api/0.6/changeset/create'
OSM_URL_OBJECT_UPLOAD = 'api/0.6/changeset/{}/upload'
OSM_URL_OBJECT_CLOSE = 'api/0.6/changeset/{}/close'
OSM_URL_NOTE = 'api/0.6/notes'
# OSM_URL = 'https://api.openstreetmap.org'
OSM_URL = 'https://master.apis.dev.openstreetmap.org'

NOMINATION_URL = 'https://nominatim.openstreetmap.org'
