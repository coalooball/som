from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('SOM_DB_NAME'),
        'USER': os.environ.get('SOM_DB_USER'),
        'PASSWORD': os.environ.get('SOM_DB_PASSWORD'),
        'HOST': os.environ.get('SOM_DB_HOST'),  
        'PORT': os.environ.get('SOM_DB_PORT'),  
    }
}