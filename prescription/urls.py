from django.urls import path

from . import views

urlpatterns = [
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('confirm_appointment/<int:pk>/', views.confirm_appointment, name='confirm_appointment'),
    path('prescribe_medicine/<int:appointment_id>/', views.prescribe_medicine, name='prescribe_medicine'),
    path('patient_prescriptions/<int:patient_id>/', views.patient_prescriptions, name='patient_prescriptions'),
]