from rest_framework import serializers
from .models import HealthRecord 



class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = ['username', 'email_id', 'record_details', 'file']