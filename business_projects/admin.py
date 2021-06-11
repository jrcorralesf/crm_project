from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import ProjectModel, SupplyModel, InventoryModel, ProductModel 

admin.site.register(ProjectModel,SimpleHistoryAdmin)
admin.site.register(SupplyModel,SimpleHistoryAdmin)
admin.site.register(InventoryModel,SimpleHistoryAdmin)
admin.site.register(ProductModel,SimpleHistoryAdmin)