"""
Django settings for ofertas project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import Csv, config
from dj_database_url import parse as db_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z8af!%i*a60(egadlcc#4-+z!s#=p(@#u=*8g1wuvtlum(gs^d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default='.localhost')

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bootstrap.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'bootstrap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASE_ENGINE = config('DATABASE_ENGINE', default='sqlite')
DATABASE_USER = config('DATABASE_USER', default='')
DATABASE_PASSWORD = config('DATABASE_PASSWORD', default='')
DATABASE_HOST = config('DATABASE_HOST', default='')
DATABASE_PORT = config('DATABASE_PORT', default='')
DATABASE_NAME = config('DATABASE_NAME', default='db.sqlite3')

DATABASE_CREDENTIALS = ''
if DATABASE_USER or DATABASE_PASSWORD or DATABASE_HOST or DATABASE_PORT:
    DATABASE_USER_PASSWORD = '{}:{}'.format(DATABASE_USER, DATABASE_PASSWORD)
    DATABASE_HOST_PORT = '{}:{}'.format(DATABASE_HOST, DATABASE_PORT)
    DATABASE_CREDENTIALS = '{}@{}'.format(DATABASE_USER_PASSWORD, DATABASE_HOST_PORT)

DATABASE_DEFAULT = '{}://{}/{}'.format(DATABASE_ENGINE, DATABASE_CREDENTIALS, DATABASE_NAME)

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default=DATABASE_DEFAULT,
        cast=db_url
    )
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = config('STATIC_ROOT')
MEDIA_ROOT = config('MEDIA_ROOT')

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default=25)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=False, cast=bool)
EMAIL_TIMEOUT = config('EMAIL_TIMEOUT', default=None)
EMAIL_FROM = config('EMAIL_FROM', default='contato@oliveiradigital.com.br')

NOTIFICATION_BACKENDS = [
    ("email", config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')),
]

DEFAULT_FROM_NAME = config('DEFAULT_FROM_NAME', default='Clube da Permuta')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default=EMAIL_FROM)

PHONENUMBER_DEFAULT_REGION = 'BR'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 5 * 3600

SITE_URL = config('SITE_URL', default='http://localhost:8000')