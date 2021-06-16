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


#CONFIGURACIÓN DE AZURE STORAGES

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_CONTAINER='contenedor-blob'
AZURE_CONNECTION_STRING='DefaultEndpointsProtocol=https;AccountName=crminteredes;AccountKey=uy4MdNj6/Vv1tNFxdSaHC3sVqSmeuQ2Yx7pR5J3M09iE7ivG5iHQQtYYgJ9Fp5f5NJvTPN11sTnfYuA1Mi+8pQ==;EndpointSuffix=core.windows.net'
AZURE_CACHE_CONTROL = "public,max-age=31536000,immutable"
#AZURE_ACCOUNT_NAME='crminteredes'
#AZURE_ACCOUNT_KEY='uy4MdNj6/Vv1tNFxdSaHC3sVqSmeuQ2Yx7pR5J3M09iE7ivG5iHQQtYYgJ9Fp5f5NJvTPN11sTnfYuA1Mi+8pQ=='
#AZURE_SSL=True
#AZURE_UPLOAD_MAX_CONN=2
#AZURE_CONNECTION_TIMEOUT_SECS=20
#AZURE_BLOB_MAX_MEMORY_SIZE=2MB
#AZURE_URL_EXPIRATION_SECS=None
#AZURE_OVERWRITE_FILES=False
#AZURE_LOCATION=''  #carpeta base
#AZURE_EMULATED_MODE=False
#AZURE_ENDPOINT_SUFFIX='core.windows.net'
#AZURE_CUSTOM_DOMAIN=''  /////////////////////// PROBANDO
#AZURE_CUSTOM_CONNECTION_STRING=AZURE_CONNECTION_STRING
#AZURE_TOKEN_CREDENTIAL='' /////////////////////// PROBANDO
'''AZURE_OBJECT_PARAMETERS={
    'content_type': '',
    'content_encoding': '', 
    'content_language': '', 
    'content_disposition': '', 
    'cache_control': '', 
    'content_md5': '',
}'''


#Configuración AWS S3
'''
AWS_ACCESS_KEY_ID = 'AKIAUYLMO7AOP7TG4SJK'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'crm-interedes-jrcorralesf'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'sa-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 
'''
