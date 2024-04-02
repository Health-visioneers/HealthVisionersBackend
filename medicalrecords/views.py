from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import  MedicalRecord, AccessPermission
from users.models import Patient , Doctor
from .forms import MedicalRecordForm, AccessPermissionForm
import os


@login_required
def create_medical_record(request):
    if request.user.is_patient and Patient.objects.filter(user=request.user).exists():
        if request.method == 'POST':
            form = MedicalRecordForm(request.POST, request.FILES)
            if form.is_valid():
                medical_record = form.save(commit=False)
                medical_record.patient = Patient.objects.get(user=request.user)
                medical_record.save()
                return redirect('medical_record_detail', pk=medical_record.pk)
        else:
            form = MedicalRecordForm()
        return render(request, 'create_medical_record.html', {'form': form})



@login_required
def medical_record_detail(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    _, extension = os.path.splitext(medical_record.record.name)
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif']
    return render(request, 'medical_record_detail.html', {'medical_record': medical_record, 'extension': extension, 'image_extensions': image_extensions})


@login_required
def update_medical_record(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, request.FILES, instance=medical_record)
        if form.is_valid():
            medical_record = form.save()
            return redirect('medical_record_detail', pk=medical_record.pk)
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'update_medical_record.html', {'form': form})

@login_required
def delete_medical_record(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        medical_record.delete()
        return redirect('medical_records')
    return render(request, 'delete_medical_record.html', {'medical_record': medical_record})

@login_required
def give_access(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = AccessPermissionForm(request.POST)
        if form.is_valid():
            access_permission = form.save(commit=False)
            access_permission.medical_record = medical_record
            access_permission.save()
            return redirect('medical_record_detail', pk=medical_record.pk)
    else:
        form = AccessPermissionForm()
    return render(request, 'give_access.html', {'form': form, 'medical_record': medical_record})

@login_required
def view_medical_record(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    now = timezone.now()
    access_permission = AccessPermission.objects.filter(medical_record=medical_record, doctor=request.user.doctor, start_time__lte=now, end_time__gte=now).first()
    if access_permission is not None:
        return render(request, 'view_medical_record.html', {'medical_record': medical_record})
    else:
        return redirect('access_denied')