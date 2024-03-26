from django.urls import path
from . import views

urlpatterns = [
    path('meeting/<int:meeting_id>/', views.meetings, name='meeting'),
    # Add more paths here
]