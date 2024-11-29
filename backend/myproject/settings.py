"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from datetime import datetime, timedelta
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get("SECRET_KEY")

SECRET_KEY = 'django-insecure-pd6ew_fx#dn^_h=ij$(dfvjw*zh(p(n+l-7+l8syd79ba#+w)!'

#SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = bool(os.environ.get("DEBUG", default=0))
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']


# Application definition

INSTALLED_APPS = [
    'accounts',
    'two_factor_auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'rest_framework_simplejwt',
]

AUTH_USER_MODEL = 'accounts.User'

##### For JWT
REST_FRAMEWORK = {
    # JWT authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),  
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # Every time a refresh token is used to generate a new access token, 
    # a new refresh token is also issued to the user.
    'ROTATE_REFRESH_TOKENS': True,
    # Old refresh tokens are blacklisted after they are replaced with new ones.
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256', # default
    # SHOULD CHANGE the SECRET_KEY when submit to security reason
    'SIGNING_KEY': SECRET_KEY,
    # Public key used to verify JWT tokens, if I use HS256 algo, it's set to none
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id', # Default, Uses 'id' as the unique identifier in JWT payload
    'USER_ID_CLAIM': 'user_id',# Default, User ID will be stored under 'user_id' in the token
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',), # default
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
}
##### For JWT


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#TEMP = os.path.join(BASE_DIR, 'media_cdn/temp')

#BASE_DIR = "http://0.0.0.0:8000"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'

# Allow the frontend domain
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
]

########## Commented 20241101
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'otxoboy64@gmail.com'
# EMAIL_HOST_PASSWORD = 'qkhw doyy kojf exss' 
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
########## Commented 20241101


# # # Setting to send a mail to gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # Gmail address (in .env file)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Gmail app password (in .env file)
# # # Setting to send a mail to gmail

LOGIN_URL = 'two_factor_auth:login' # # # not implemented yet

ACTIVATE_URL = 'http://localhost:8000/accounts'


# # # Session engine to use redis
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_SECURE = False  # Set to True for HTTPS
SESSION_SAVE_EVERY_REQUEST = True  # Ensure session is saved on every request
SESSION_COOKIE_AGE = 3600


# Cache configuration to point to Redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",  # Redis URL (matches the Redis service name in Docker Compose)
    # "LOCATION": f"redis://{os.environ.get('REDIS_HOST', 'redis')}:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Set the session engine to use the database

# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# settings.py
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"
# SESSION_COOKIE_AGE = 300  # Session lasts for 5 minutes, adjust as needed
# SESSION_SAVE_EVERY_REQUEST = True  # Optional: Save session data on each request


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]