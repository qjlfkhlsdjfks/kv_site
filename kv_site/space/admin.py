from django.contrib import admin
from space.models import Place, Category 


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rate')


admin.site.register(Place, PlaceAdmin)
admin.site.register(Category)
