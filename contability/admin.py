from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import (
    ContabilityModel, PayrollModel, SellModel, BillModel, 
    InvoicingModel, InventoryConceptModel, DiscountModel, 
    PurchaseModel, PurchaseOrderModel
    )


admin.site.register(ContabilityModel,SimpleHistoryAdmin)
admin.site.register(PayrollModel,SimpleHistoryAdmin)
admin.site.register(SellModel,SimpleHistoryAdmin)
admin.site.register(BillModel,SimpleHistoryAdmin)
admin.site.register(InvoicingModel,SimpleHistoryAdmin)
admin.site.register(InventoryConceptModel,SimpleHistoryAdmin)
admin.site.register(DiscountModel,SimpleHistoryAdmin)
admin.site.register(PurchaseModel,SimpleHistoryAdmin)
admin.site.register(PurchaseOrderModel,SimpleHistoryAdmin)

