from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import Appointment, Prescription, Medicine
from .forms import AppointmentForm, PrescriptionForm
from users.models import Patient, Doctor
from django.views import View

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            patient = Patient.objects.get(user__email=request.user.email)
            appointment.patient = patient
            # Save patient id here
            appointment.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})





def times():
    return [(f'{i:02d}:{j:02d}', f'{i:02d}:{j:02d}') for i in range(8, 21) for j in range(0, 60, 15)]

def get_available_times(request):
    date = request.GET.get('date')
    date = datetime.strptime(date, '%Y-%m-%d').date()  # Convert the date string to a date object

    # Get all appointments for the given date
    appointments = Appointment.objects.filter(date=date)

    # Get all time slots
    all_times = times()
    # Exclude the times of the existing appointments
    for appointment in appointments:
        start_time = f'{appointment.start_time.hour:02d}:{appointment.start_time.minute:02d}'
        end_time = f'{appointment.end_time.hour:02d}:{appointment.end_time.minute:02d}'
        all_times = [time for time in all_times if time[0] < start_time or time[0] >= end_time]
     
    available = []   
    for time in all_times:
        available.append(time[0])
    return JsonResponse(available, safe=False)

def appointment_list(request):
    if request.user.is_authenticated:
        try:
            if request.user.is_patient:
                # If the user is a patient, retrieve their appointments , order by latest
                appointments = Appointment.objects.filter(patient=request.user.patient).order_by('-date')
            elif request.user.is_doctor:
                # If the user is a doctor, retrieve their appointments
                appointments = Appointment.objects.filter(doctor=request.user.doctor).order_by('-date')
            else:
                appointments = []
        except (Patient.DoesNotExist, Doctor.DoesNotExist):
            appointments = []
    else:
        appointments = []
    return render(request, 'appointments.html', {'appointments': appointments})

# Create your views here.

@login_required()
def confirm_appointment(request, pk):
    if request.user.is_authenticated and request.user.is_doctor:
        appointment = Appointment.objects.get(pk=pk)
        if appointment.doctor == request.user.doctor:
            appointment.status = True
            appointment.confirmed = True
            appointment.save()
            return redirect('appointments')
        else:
            messages.error(request, 'Error: This appointment does not belong to you.')
            return redirect('appointments')
    else:
        messages.error(request, 'Error: You do not have permission to confirm this appointment.')
        return redirect('appointments')
    

@login_required()
def cancel_appointment(request, pk):
    if request.user.is_authenticated and request.user.is_doctor:
        appointment = Appointment.objects.get(pk=pk)
        if appointment.doctor == request.user.doctor:
            appointment.status = True
            appointment.confirmed = False
            appointment.save()
            return redirect('appointments')
        else:
            messages.error(request, 'Error: This appointment does not belong to you.')
            return redirect('appointments')
    else:
        messages.error(request, 'Error: You do not have permission to cancel this appointment.')
        return redirect('appointments')






def prescribe_medicine(request, appointment_id):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        prescription = request.POST.getlist('medicines')
        
        for medicine_id in prescription:
            prescription = Prescription(appointment_id=appointment_id, medicine_id=medicine_id)
            prescription.save()
            
        # Redirect to the details page for the appointment
        appointment = Appointment.objects.filter(id= appointment_id).update(prescription=True)
        appointment.save()
        
        return redirect('appointments')
    else:
        appointment = get_object_or_404(Appointment, pk=appointment_id)
        patient = appointment.patient
        print(patient)
        
    return render(request, 'select_medcines.html', {'appointment_id': appointment_id, 'patient': patient})


def patient_prescriptions(request, appointment_id):
    prescriptions = Prescription.objects.filter(appointment__id=appointment_id)
    return render(request, 'patient_prescriptions.html', {'prescriptions': prescriptions})




class SearchMedicineView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        medicines = Medicine.objects.filter(
            Q(name__icontains=query) |
            Q(manufacturer__icontains=query) |
            Q(type__icontains=query) 
            # | Q(short_composition1__icontains=query) 
            # | Q(short_composition2__icontains=query)
        )
        medicines_json = list(medicines.values('id', 'name'))
        return JsonResponse(medicines_json, safe=False)