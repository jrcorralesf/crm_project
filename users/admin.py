from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.admin import UserAdmin

from .models import RoleModel, UserModel

admin.site.register(RoleModel,SimpleHistoryAdmin)
admin.site.register(UserModel,SimpleHistoryAdmin)