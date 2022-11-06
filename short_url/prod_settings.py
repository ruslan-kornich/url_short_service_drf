import os.path
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'sdjhue493482hdjsd0ae8*x3t!(2^j0nsojhv+&b&jub1i2v5jtmap5g)z#7z9(8ymc'

DEBUG = False

ALLOWED_HOSTS = []


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static", ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'short',
        'USER': 'userdb',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
