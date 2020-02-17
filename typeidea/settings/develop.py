from .base import * #NOQA

DEBUG = True
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
#         'ENGINE':'django.db.backends.mysql',
        'NAME':os.path.join(BASE_DIR,'db.sqlite3'),
        }
    }