from django.urls import path
from . import views

urlpatterns = [
    path('meeting/', views.meetings, name='meeting'),
    # Add more paths here
]