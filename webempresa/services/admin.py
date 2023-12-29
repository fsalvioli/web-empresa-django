from django.contrib import admin
from .models import Service
# Register your models here.
# Esta clase nos ayuda a que algunos campos que Django oculta por defecto, puedan ser vistos. En este caso como solo lectura.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)