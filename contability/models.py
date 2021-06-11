import uuid

from django.db import models

from simple_history.models import HistoricalRecords



class ContabilityModel(models.Model):
    total_balance=models.DecimalField(max_digits=15, decimal_places=2)
    payroll = models.OneToOneField('PayrollModel', on_delete=models.CASCADE)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Contabilidad'
        verbose_name_plural = 'Contabilidad'

    def __str__(self):
        return f'| id: {self.pk} '

class PayrollModel(models.Model):
    total_amount=models.DecimalField(max_digits=14, decimal_places=2)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Nómina'
        verbose_name_plural = 'Nómina'

    def __str__(self):
        return f'| id: {self.pk} '

class SellModel(models.Model):
    contability = models.ForeignKey('ContabilityModel', on_delete=models.CASCADE)
    bill = models.OneToOneField('BillModel', on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digits=12, decimal_places=2)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return f'| id: {self.pk} '

class BillModel(models.Model):
    final_price=models.DecimalField(max_digits=10, decimal_places=2)
    final_discounts=models.DecimalField(max_digits=8, decimal_places=2)
    quantity=models.SmallIntegerField()

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Orden de venta (factura)'
        verbose_name_plural = 'Ordenes de venta (facturas)'

    def __str__(self):
        return f'| id: {self.pk} '

class BillModel(models.Model):
    final_price=models.DecimalField(max_digits=10, decimal_places=2)
    final_discounts=models.DecimalField(max_digits=8, decimal_places=2)
    quantity=models.SmallIntegerField()

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Concepto de venta (factura)'
        verbose_name_plural = 'Conceptos de venta (facturas)'

    def __str__(self):
        return f'| id: {self.pk} '

class InvoicingModel(models.Model):
    billing_concept = models.OneToOneField('BillModel', on_delete=models.CASCADE)
    inventory_concept = models.OneToOneField('InventoryConceptModel', on_delete=models.CASCADE) 

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Facturación'
        verbose_name_plural = 'Facturaciones'

    def __str__(self):
        return f'| id: {self.pk} '

class InventoryConceptModel(models.Model):
    code = models.CharField(max_length=80)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discounts = models.ManyToManyField('DiscountModel')

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Concepto de inventario'
        verbose_name_plural = 'Conceptos de inventario'

    def __str__(self):
        return f'| id: {self.pk} '

class DiscountModel(models.Model):
    code = models.CharField(max_length=80)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'

    def __str__(self):
        return f'| id: {self.pk} '

class PurchaseModel(models.Model):
    contability = models.ForeignKey('ContabilityModel', on_delete=models.CASCADE)
    purchase_order = models.OneToOneField('PurchaseOrderModel', on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digits=12, decimal_places=2)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        return f'| id: {self.pk} '

class PurchaseOrderModel(models.Model):
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.SmallIntegerField()

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Ordenes de Compra'

    def __str__(self):
        return f'| id: {self.pk} '