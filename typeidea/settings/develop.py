from .base import * #NOQA

DEBUG = True
DATABASES = {
    'default':{
#         'ENGINE':'django.db.backends.sqlite3',
#         'NAME':os.path.join(BASE_DIR,'db.sqlite3'),
        'ENGINE':'django.db.backends.mysql',
        'NAME':'typeidea_db',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'POST':3306

        }
    }