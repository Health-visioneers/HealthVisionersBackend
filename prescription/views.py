from django.shortcuts import render, redirect
from .models import Appointment, Prescription
from .forms import AppointmentForm
from users.models import Patient

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            patient = Patient.objects.get(user__email=request.user.email)
            appointment.patient = patient
            # Save patient id here
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

from django.shortcuts import render
from .models import Appointment, Patient, Doctor

def appointment_list(request):
    if request.user.is_authenticated:
        try:
            if request.user.is_patient:
                # If the user is a patient, retrieve their appointments
                appointments = Appointment.objects.filter(patient=request.user.patient)
            elif request.user.is_doctor:
                # If the user is a doctor, retrieve their appointments
                appointments = Appointment.objects.filter(doctor=request.user.doctor)
            else:
                appointments = []
        except (Patient.DoesNotExist, Doctor.DoesNotExist):
            appointments = []
    else:
        appointments = []

    return render(request, 'appointments.html', {'appointments': appointments})

# Create your views here.
def confirm_appointment(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    appointment.confirmed = True
    appointment.save()
    return redirect('appointment_list')



from .forms import PrescriptionForm

def prescribe_medicine(request, appointment_id):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.appointment_id = appointment_id
            prescription.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'prescribe_medicine.html', {'form': form})


def patient_prescriptions(request, patient_id):
    prescriptions = Prescription.objects.filter(appointment__patient_id=patient_id)
    return render(request, 'patient_prescriptions.html', {'prescriptions': prescriptions})