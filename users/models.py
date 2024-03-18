from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid
import hashlib

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_hospital_staff = models.BooleanField(default=False)
    

class Patient(models.Model):
    id = models.UUIDField( default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='patient')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    medical_record_number = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Generate MD5 hash
        hash_string = f"{self.id}{self.first_name}{self.last_name}{self.user.email}"
        md5_hash = hashlib.md5(hash_string.encode()).hexdigest()
        # Set the medical_record_number field to the MD5 hash
        self.medical_record_number = md5_hash
        super().save(*args, **kwargs)
        
        
        
class Doctor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    years_of_experience = models.IntegerField(null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='doctors' , default=None)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, related_name='doctors')
    created_at = models.DateTimeField(default=timezone.now)


class HospitalStaff(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='staff')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='staff')
    hire_date = models.DateField(auto_now_add=True, null=True, blank=True)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, related_name='staff')
    created_at = models.DateTimeField(default=timezone.now)


class Hospital(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=20)
    website = models.URLField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    num_doctors = models.IntegerField(null=True, blank=True)
    num_staff = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    departments = models.ManyToManyField('Department', related_name='hospitals')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name



class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
