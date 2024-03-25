from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Appointment, Medicine, Prescription

class AppointmentResource(resources.ModelResource):
    class Meta:
        model = Appointment
        fields = ('id', 'doctor', 'patient', 'description', 'date', 'start_time', 'end_time', 'status', 'confirmed', 'meeting_id')

class AppointmentAdmin(ImportExportModelAdmin):
    resource_class = AppointmentResource
    list_display = ('doctor', 'patient', 'date', 'status', 'confirmed')
    search_fields = ('doctor__name', 'patient__name')
    list_filter = ('status', 'confirmed')

class MedicineResource(resources.ModelResource):
    class Meta:
        model = Medicine
        fields = ('id', 'name', 'price', 'is_discontinued', 'manufacturer', 'type', 'pack_size_label', 'short_composition1', 'short_composition2')

class MedicineAdmin(ImportExportModelAdmin):
    resource_class = MedicineResource
    list_display = ('name', 'price', 'is_discontinued', 'manufacturer', 'type')
    search_fields = ('name', 'manufacturer', 'type')
    list_filter = ('is_discontinued',)

class PrescriptionResource(resources.ModelResource):
    class Meta:
        model = Prescription
        fields = ('id', 'appointment', 'medicine', 'dosage', 'days_to_take', 'times_per_day', 'instructions')

class PrescriptionAdmin(ImportExportModelAdmin):
    resource_class = PrescriptionResource
    list_display = ('appointment', 'medicine', 'dosage', 'days_to_take', 'times_per_day')
    search_fields = ('appointment__doctor__name', 'medicine__name')
    list_filter = ('medicine',)

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Prescription, PrescriptionAdmin)