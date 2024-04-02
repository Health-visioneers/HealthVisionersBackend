from django import forms
from .models import MedicalRecord, AccessPermission

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['record']

class AccessPermissionForm(forms.ModelForm):
    class Meta:
        model = AccessPermission
        fields = ['doctor', 'start_time', 'end_time']