from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Appointment , Prescription
from datetime import datetime

def times():
    return [(f'{i:02d}:{j:02d}', f'{i:02d}:{j:02d}') for i in range(8, 21) for j in range(0, 60, 15)]


class AppointmentForm(forms.ModelForm):
    # date = forms.DateField(widget=forms.SelectDateWidget(attrs={'id': 'date'}))
    start_time = forms.TimeField(widget=forms.Select(choices=times(), attrs={'id': 'start_time'}))
    end_time = forms.TimeField(widget=forms.Select(choices=times(), attrs={'id': 'end_time'}))

    class Meta:
        model = Appointment
        fields = ['doctor', 'description' , 'date' , 'start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        doctor = cleaned_data.get('doctor')

        if date and date < datetime.now().date():
            self.add_error('date', ValidationError("The date cannot be in the past."))

        if start_time and (start_time.hour < 8 or start_time.hour >= 21):
            self.add_error('start_time', ValidationError("The appointment must start between 8 AM and 9 PM."))

        if end_time and (end_time.hour < 8 or end_time.hour > 21):
            self.add_error('end_time', ValidationError("The appointment must end between 8 AM and 9 PM."))

        if start_time and end_time and start_time >= end_time:
            self.add_error('end_time', ValidationError("End time must be after start time."))

        if doctor and Appointment.objects.filter(doctor=doctor, date=date, start_time=start_time, end_time=end_time).exists():
            self.add_error(None, ValidationError("There is already an appointment at this time."))

        return cleaned_data



