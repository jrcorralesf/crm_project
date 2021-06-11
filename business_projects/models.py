import uuid

from django.db import models

from simple_history.models import HistoricalRecords

from users.employ_models import EmployModel

class ProjectModel(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    supplies = models.ManyToManyField('SupplyModel')
    inventory = models.ManyToManyField('InventoryModel')
    employess = models.ManyToManyField(EmployModel)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return f'| id: {self.pk} '


class SupplyModel(models.Model):  #al crear un insumo se disminuye el stock
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('ProductModel')

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

    def __str__(self):
        return f'| id: {self.pk} '

class InventoryModel(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('ProductModel')

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

    def __str__(self):
        return f'| id: {self.pk} '

class ProductModel(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField()

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.name}| stock:{self.stock} | id: {self.pk} '