from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'


AWS_ACCESS_KEY_ID = 'AKIAUYLMO7AOP7TG4SJK'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'crm-interedes-jrcorralesf'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'sa-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 

