from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../development/rpg_blog/db.sqlite3'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, '../../data/rpg_blog/media/')
