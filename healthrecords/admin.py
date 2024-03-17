from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import HealthRecord


class HealthRecordAdmin(ImportExportModelAdmin):
    list_display = ('username', 'email_id', 'record_details')  # fields to display
    search_fields = ('username', 'email_id')  # fields to search
    list_filter = ('username',)  # fields to filter

admin.site.register(HealthRecord, HealthRecordAdmin)