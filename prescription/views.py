from django.shortcuts import render, redirect
from .models import Appointment, Prescription
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})



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