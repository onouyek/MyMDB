from config.common_settings import *

DEBUG = True

SECRET_KEY = '_&@#veo_(o4nr^2cv2%*5isnk(ur!(o7*ttei^-#_wu4+(h#p1'

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]