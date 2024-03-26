from django.urls import path

from . import views

urlpatterns = [
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.appointment_list, name='appointments'),
    path('get_available_times/', views.get_available_times, name='get_available_times' ),
    path('confirm_appointment/<int:pk>/', views.confirm_appointment, name='confirm_appointment'),
    path('cancel_appointment/<int:pk>/', views.cancel_appointment, name='cancel_appointment'),
    path('prescribe_medicine/<int:appointment_id>/', views.prescribe_medicine, name='prescribe_medicine'),
    path('patient_prescriptions/<int:appointment_id>/', views.patient_prescriptions, name='patient_prescriptions'),
    path('search_medicines/', views.SearchMedicineView.as_view(), name='search_medicines'),
]

