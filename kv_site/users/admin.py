from django.contrib import admin
from users.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login')


admin.site.register(User, UserAdmin)
