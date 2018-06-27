from config.common_settings import *

DEBUG = True

SECRET_KEY = '_&@#veo_(o4nr^2cv2%*5isnk(ur!(o7*ttei^-#_wu4+(h#p1'

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES['default'].update({
    'NAME': 'mymdb',
    'USER': 'mymdb',
    'PASSWORD': 'development',
    'HOST': 'localhost',
    'PORT': '5432',
})

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-locmemcache',
        'TIMEOUT': 5,
    }
}

# file uploads

MEDIA_ROOT = os.path.join(
    BASE_DIR, '../media_root')

INTERNAL_IPS = [
    '127.0.0.1',
]
