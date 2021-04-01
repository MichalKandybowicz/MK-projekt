import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

DEBUG = os.environ.get('DEBUG', True)  # False


SECRET_KEY = '43)%4yx)aa@a=+_csr3(fn&ewkf3g29xax+=+a&key9i=!98zyim=8j'
