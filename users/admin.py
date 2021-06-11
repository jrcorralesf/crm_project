from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import RoleModel, UserModel
from .employ_models import (
        EmployModel,
        EmployContractModel, ContractModel, PositionModel, EndowmentModel, AreaModel,
        EmployHealthModel, HealthModel, 
        EmployRiskModel, RiskModel, 
        EmployPensionModel, PensionModel,
        AidModel
        )

admin.site.register(RoleModel,SimpleHistoryAdmin)
admin.site.register(UserModel,SimpleHistoryAdmin)

admin.site.register(EmployModel,SimpleHistoryAdmin)
admin.site.register(EmployContractModel,SimpleHistoryAdmin)
admin.site.register(ContractModel,SimpleHistoryAdmin)
admin.site.register(PositionModel,SimpleHistoryAdmin)
admin.site.register(EndowmentModel,SimpleHistoryAdmin)
admin.site.register(AreaModel,SimpleHistoryAdmin)
admin.site.register(EmployHealthModel,SimpleHistoryAdmin)
admin.site.register(HealthModel,SimpleHistoryAdmin)
admin.site.register(EmployRiskModel,SimpleHistoryAdmin)
admin.site.register(RiskModel,SimpleHistoryAdmin)
admin.site.register(EmployPensionModel,SimpleHistoryAdmin)
admin.site.register(PensionModel,SimpleHistoryAdmin)
admin.site.register(AidModel,SimpleHistoryAdmin)