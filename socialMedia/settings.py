"""
Django settings for socialMedia project.

Generated by 'django-admin startproject' using Django 1.11.29.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from pathlib import Path

import os
import django_heroku
import dj_database_url
DATABASES = { 'default': dj_database_url.config() }
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')x_8es_g+vjv0ep@l_vfcjx!^@i$g(ie!(l72xlqk2)k=jzp^7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'accounts',
    'msgnotifications',
    'groups',
    'friend',
    'active_link',
    'profanitycustom',
    'crispy_forms',

    
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'accounts.middleware.AnonymousMiddleWare',

]

ROOT_URLCONF = 'mxh2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'mxh2.wsgi.application'


#postgres://btrtyuulpdbwuq:587c980fffe54ca67f9c1aaf24cb07ca33f0aac86924742cc1c4431bb2bdda55@ec2-34-196-238-94.compute-1.amazonaws.com:5432/d479jhcc9pdd6q

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'detq9so7h3su3f',
        'USER': 'fcxynhfcvqadct',
        'PASSWORD': 'e235369c60f829629fde23cade08feef9da5b3b78cecf40e32fcaa850e4bc39c',
        'HOST': 'ec2-18-214-214-252.compute-1.amazonaws.com',
        'PORT': 5432,
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
#postgres://fcxynhfcvqadct:e235369c60f829629fde23cade08feef9da5b3b78cecf40e32fcaa850e4bc39c@ec2-18-214-214-252.compute-1.amazonaws.com:5432/detq9so7h3su3f

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

LOGIN_REDIRECT_URL = '/posts/'
# LOGIN_URL='/posts/'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_L10N = True

USE_TZ = True
AUTH_EXEMPT_ROUTES = ('signup',
                     'login', 
                     'password_reset',
                     'password_reset_done',
                     'password_reset_confirm',
                     'password_reset_complete',
                     'password_change',
                     'password_change_done',
                     'admin',
                     )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL='/images/'

MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')

# MEDIA_ROOT = os.path.join(BASE_DIR, 'posts/static/images')

django_heroku.settings(locals())
