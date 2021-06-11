import uuid

from django.db import models

from simple_history.models import HistoricalRecords

from .models import UserModel
#from business_projects.models import ProductModel
#from contability.models import PayrollModel


class EmployModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    payroll = models.ForeignKey('contability.PayrollModel', on_delete=models.CASCADE)
    contract = models.OneToOneField('EmployContractModel', on_delete=models.CASCADE)
    health = models.OneToOneField('EmployHealthModel', on_delete=models.CASCADE)
    risk = models.OneToOneField('EmployRiskModel', on_delete=models.CASCADE)
    pension = models.OneToOneField('EmployPensionModel', on_delete=models.CASCADE)
    salary_aid = models.ManyToManyField('AidModel')
    total_salary = models.PositiveIntegerField()

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'| id: {self.pk} '


class EmployContractModel(models.Model):
    contract = models.OneToOneField('ContractModel', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Empleado-contrato'
        verbose_name_plural = 'Empleado-contrato'

    def __str__(self):
        return f'| id: {self.pk} '

class ContractModel(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    job_position = models.ForeignKey('PositionModel', on_delete=models.CASCADE)
    contents = models.TextField()

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return f'| id: {self.pk} '

class PositionModel(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    base_salary = models.PositiveIntegerField()
    endowment = models.ForeignKey('EndowmentModel', on_delete=models.CASCADE) 
    job_area= models.ManyToManyField('AreaModel')

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Cargo de trabajo'
        verbose_name_plural = 'Cargo de trabajo'

    def __str__(self):
        return f'| id: {self.pk} '

class EndowmentModel(models.Model): #al crear una dotación se disminuye el stock
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('business_projects.ProductModel')

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Dotacion'
        verbose_name_plural = 'Dotaciones'

    def __str__(self):
        return f'| id: {self.pk} '

class AreaModel(models.Model):
    name = models.CharField(max_length=80)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Área de trabajo'
        verbose_name_plural = 'Áreas de trabajo'

    def __str__(self):
        return f'| id: {self.pk} '

class EmployHealthModel(models.Model):
    health_service = models.OneToOneField('HealthModel', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    cost_amount = models.DecimalField(max_digits=12, decimal_places=2)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Empleado-servicio de salud'
        verbose_name_plural = 'Empleado-servicios de salud'
    def __str__(self):
        return f'| id: {self.pk} '

class HealthModel(models.Model):
    name = models.CharField(max_length=80)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Servicio de salud'
        verbose_name_plural = 'Servicios de salud'

    def __str__(self):
        return f'| id: {self.pk} '
class EmployRiskModel(models.Model):
    risk_service = models.OneToOneField('RiskModel', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    cost_amount = models.DecimalField(max_digits=12, decimal_places=2)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Empleado-servicio de riesgo'
        verbose_name_plural = 'Empleado-servicios de riesgo'

    def __str__(self):
        return f'| id: {self.pk} '
class RiskModel(models.Model):
    name = models.CharField(max_length=80)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Servicio de riesgo'
        verbose_name_plural = 'Servicios de riesgo'

    def __str__(self):
        return f'| id: {self.pk} '

class EmployPensionModel(models.Model):
    pension_service = models.OneToOneField('PensionModel', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    cost_amount = models.DecimalField(max_digits=12, decimal_places=2)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Empleado-servicio de pensión'
        verbose_name_plural = 'Empleado-servicios de pensión'

    def __str__(self):
        return f'| id: {self.pk} '

class PensionModel(models.Model):
    name = models.CharField(max_length=80)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Servicio de pensión'
        verbose_name_plural = 'Servicios de pensión'

    def __str__(self):
        return f'| id: {self.pk} '


class AidModel(models.Model):
    reason = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Auxilio salarial'
        verbose_name_plural = 'Auxilios salariales'

    def __str__(self):
        return f'| id: {self.pk} '

