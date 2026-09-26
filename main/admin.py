from django.contrib import admin
from . import models

@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address']
    search_fields = ['user__username', 'address']