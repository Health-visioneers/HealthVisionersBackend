from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Doctor, Patient
import random


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    status = models.BooleanField(default=False, help_text="false if the appointment is Pending")
    confirmed = models.BooleanField(default=False, help_text="True if the appointment is confirmed")
    meeting_id = models.IntegerField(unique=True, null=True)
    prescribed = models.BooleanField(default=False)

    @staticmethod
    def generate_unique_meeting_id():
        while True:
            random_id = random.randint(100000, 999999)
            if not Appointment.objects.filter(meeting_id=random_id).exists():
                return random_id

    def save(self, *args, **kwargs):
        if not self.meeting_id:
            self.meeting_id = Appointment.generate_unique_meeting_id()
        super().save(*args, **kwargs)



class Medicine(models.Model):
    name = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=2 ,  blank=True, null=True)
    is_discontinued = models.BooleanField(default=False)
    manufacturer = models.CharField(max_length=255 , blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    pack_size_label = models.CharField(max_length=255, blank=True, null=True)
    short_composition1 = models.CharField(max_length=255, blank=True, null=True)
    short_composition2 = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=255, blank=True, null=True, help_text="Dosage instructions, e.g., '2 tablets'")
    days_to_take = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True, help_text="Number of days to take the medicine")
    times_per_day = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], blank=True, null=True, help_text="Number of times to take the medicine per day")
    instructions = models.TextField(blank=True,  null=True, help_text="Any additional instructions")

    class Meta:
        verbose_name = "Prescription"
        verbose_name_plural = "Prescriptions"

    def __str__(self):
        return f"{self.medicine.name}"

    def total_doses(self):
        return self.days_to_take * self.times_per_day
    
