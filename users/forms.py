from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Department, Hospital, Patient, Doctor, HospitalStaff, User
from django.utils import timezone


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'address']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialty', 'license_number', 'years_of_experience', 'hospital', 'department']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hospital'].queryset = Hospital.objects.filter(is_active=True)

class HospitalStaffForm(forms.ModelForm):
    class Meta:
        model = HospitalStaff
        fields = ['first_name', 'last_name', 'position', 'department', 'hospital']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hospital'].queryset = Hospital.objects.filter(is_active=True)