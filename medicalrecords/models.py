from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.base import ContentFile
from users.models import Doctor, Patient
from simple_history.models import HistoricalRecords


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, related_name='medical_records', on_delete=models.CASCADE)
    record = models.FileField(upload_to='medical_records/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    

    def __str__(self):
        return f'{self.patient.user.username} - {self.created_at}'

class AccessPermission(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, related_name='access_permissions', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='access_permissions', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    history = HistoricalRecords()
    

    def __str__(self):
        return f'{self.medical_record.patient.user.username} - {self.doctor.user.username}'