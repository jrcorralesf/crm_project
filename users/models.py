import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser 

from django_countries.fields import CountryField
from simple_history.models import HistoricalRecords

from .utils import get_document_choices

class RoleModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50,unique=True)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Rol (grupo)'
        verbose_name_plural = 'Roles (grupos)'

    def __str__(self):
        return f'Rol: {self.name} | id: {self.pk} '

class UserModel(AbstractUser):
    identification_document_type = models.CharField(max_length=3,choices=get_document_choices(),default='CC')
    number_of_identification = models.PositiveIntegerField(primary_key=True) 
    roles = models.ManyToManyField(RoleModel)
    is_employ = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    nationality = CountryField(blank_label='(seleccione su pais de nacimiento)')
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    
    history = HistoricalRecords()
    
    REQUIRED_FIELDS = ['email','roles','first_name','last_name','identification_document_type',
                'number_of_identification','nationality','birth_date']
    #USERNAME_FIELD = 'username' # por defecto es username (no pueden haber 2 repetidos)
        
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.first_name} {self.last_name} | id= {self.pk}'
