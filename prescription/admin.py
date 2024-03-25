from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Medicine

class MedicineResource(resources.ModelResource):
    class Meta:
        model = Medicine
        fields = ('id', 'name', 'price', 'is_discontinued', 'manufacturer', 'type', 'pack_size_label', 'short_composition1', 'short_composition2')

class MedicineAdmin(ImportExportModelAdmin):
    resource_class = MedicineResource
    list_display = ('name', 'price', 'is_discontinued', 'manufacturer', 'type', 'pack_size_label', 'short_composition1', 'short_composition2')
    search_fields = ('name', 'manufacturer', 'type')
    list_filter = ('is_discontinued',)

admin.site.register(Medicine, MedicineAdmin)