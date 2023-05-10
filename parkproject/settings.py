"""
Django settings for parkproject project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from . import settings_prod
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings_prod.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS =['localhost']
ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.utils.translation',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'lang',
    'useri.apps.UseriAppConfig',
    'clienti.apps.ClientiAppConfig',
    'staff.apps.StaffAppConfig',
    'plati',
    'parcare',
    'django.contrib.admin',
    'django.contrib.auth',
    'rosetta',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'parkproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'parkproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ro'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('ro', _('Romana')),
    ('it', _('Italiano')),
    ('en', _('English')),

)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"


MEDIA_URL = '/staticfiles/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/images/')
MEDIA_ROOT_LOGO = os.path.join(BASE_DIR, 'staticfiles/parkproject/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = "/useri/login"
LOGIN_REDIRECT_URL = "/"


# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = BASE_DIR / 'sent_emails/'

EMAIL_BACKEND = settings_prod.EMAIL_BACKEND
EMAIL_HOST = settings_prod.EMAIL_HOST
EMAIL_FROM = settings_prod.EMAIL_FROM
EMAIL_HOST_USER = settings_prod.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = settings_prod.EMAIL_HOST_PASSWORD
EMAIL_PORT = settings_prod.EMAIL_PORT
EMAIL_USE_TLS = settings_prod.EMAIL_USE_TLS

PASSWORD_RESET_TIMEOUT = settings_prod.PASSWORD_RESET_TIMEOUT


STRIPE_PUBLISHABLE_KEY = settings_prod.STRIPE_PUBLISHABLE_KEY
STRIPE_SECRET_KEY = settings_prod.STRIPE_SECRET_KEY