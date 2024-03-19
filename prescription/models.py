from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Doctor, Patient


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.BooleanField(default=False, help_text="True if the appointment is confirmed")
    # other fields...

    def __str__(self):
        return f"Appointment on {self.date} with {self.doctor.name}"


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    # other fields...

    def __str__(self):
        return self.name

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=255, help_text="Dosage instructions, e.g., '2 tablets'")
    days_to_take = models.IntegerField(validators=[MinValueValidator(1)], help_text="Number of days to take the medicine")
    times_per_day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(24)], help_text="Number of times to take the medicine per day")
    instructions = models.TextField(blank=True, help_text="Any additional instructions")

    class Meta:
        verbose_name = "Prescription"
        verbose_name_plural = "Prescriptions"

    def __str__(self):
        return f"{self.medicine.name} for {self.days_to_take} days"

    def total_doses(self):
        return self.days_to_take * self.times_per_day