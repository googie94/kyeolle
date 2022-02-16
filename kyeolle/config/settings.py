# from pathlib import Path
import json
import sys
import os
from decouple import config

# 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
# CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
# CONFIG_SECRET_BASE_FILE = os.path.join(CONFIG_SECRET_DIR, 'base.json')
# CONFIG_SECRET_BASE_FILE = os.path.join(CONFIG_SECRET_DIR, '.env')
# CONFIG_SECRET_DEVELOPMENT_FILE = os.path.join(CONFIG_SECRET_DIR, 'development.json')
# CONFIG_SECRET_PRODUCTION_FILE = os.path.join(CONFIG_SECRET_DIR, 'production.json')
# config_secret_base = json.loads(open(CONFIG_SECRET_BASE_FILE).read())


# 
# SECRET_KEY = config_secret_base['django']['secret_key']
SECRET_KEY = config("DJANGO_SECRET_KEY")
# DEBUG = config_secret_base['django']['debug']
DEBUG = config("DEBUG")
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'web',
]

# 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 
ROOT_URLCONF = 'config.urls'

# 
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

# 
WSGI_APPLICATION = 'config.wsgi.application'

# 
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        # "NAME": config_secret_base['database']['name'],
        # "USER": config_secret_base['database']['user'],
        # "PASSWORD": config_secret_base['database']['password'],
        # "HOST": config_secret_base['database']['host'],
        # "PORT": config_secret_base['database']['port'],
        "NAME": config("MYSQL_NAME"),
        "USER": config("MYSQL_USER"),
        "PASSWORD": config("MYSQL_PASSWORD"),
        "HOST": config("MYSQL_HOST"),
        "PORT": config("MYSQL_PORT")
    }
}

# 
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

# 
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
