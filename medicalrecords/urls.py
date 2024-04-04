from django.urls import path
from . import views

urlpatterns = [
    path('create_medical_record/', views.create_medical_record, name='create_medical_record'),
    path('medical_record/<int:pk>/', views.medical_record_detail, name='medical_record_detail'),
    path('update_medical_record/<int:pk>/', views.update_medical_record, name='update_medical_record'),
    path('delete_medical_record/<int:pk>/', views.delete_medical_record, name='delete_medical_record'),
    path('give_access/<int:pk>/', views.give_access, name='give_access'),
    path('view_medical_record/<int:pk>/', views.view_medical_record, name='view_medical_record'),
    path('medicalrecords/' , views.display_records, name='medicalrecords')
]