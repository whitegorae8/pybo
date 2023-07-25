from .base import *

ALLOWED_HOSTS = ['54.180.64.207', 'assist-8.com']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'iY0>(J]V:KAoWv0hp$9h^yzMuFp)^8ty',
        'HOST': 'ls-b85d0f54303b34b782d62b0a219fc938d131bf81.cpqu19dtplyc.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
