from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Patient, Doctor, HospitalStaff, Hospital, Department , User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active', 'date_joined')



class PatientAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'medical_record_number', 'date_of_birth', 'address', 'created_at')
    search_fields = ('first_name', 'last_name', 'medical_record_number')
    list_filter = ('created_at',)

class DoctorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'specialty', 'license_number', 'years_of_experience', 'hospital', 'created_at')
    search_fields = ('first_name', 'last_name', 'specialty', 'license_number')
    list_filter = ('specialty', 'hospital', 'created_at',)

class HospitalStaffAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'position', 'department', 'hire_date', 'hospital', 'created_at')
    search_fields = ('first_name', 'last_name', 'position', 'department')
    list_filter = ('position', 'department', 'hospital', 'hire_date', 'created_at',)

class HospitalAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'address', 'contact_number', 'website', 'capacity', 'num_doctors', 'num_staff', 'rating', 'is_active', 'created_at')
    search_fields = ('name', 'address', 'contact_number', 'website')
    list_filter = ('is_active', 'created_at',)

class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(HospitalStaff, HospitalStaffAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(User, UserAdmin)