from .base import *

ALLOWED_HOSTS = ['www.rpg.nathanhare.net',
    'rpg.nathanhare.net',
    'rpg2.nathanhare.net',
    'www.rpg2.nathanhare.net',
]

STATIC_ROOT = '/srv/http/rpg_blog/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '../../../data/rpg_blog/media/')
