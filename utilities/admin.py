from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import ServiceRequest

def mark_resolved(modeladmin, request, queryset):
    queryset.update(status='resolved')

mark_resolved.short_description = "Mark selected requests as resolved"

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['type', 'details', 'status']
    actions = [mark_resolved]

admin.site.register(ServiceRequest, ServiceRequestAdmin)