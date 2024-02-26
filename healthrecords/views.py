from django.shortcuts import render

from rest_framework import viewsets
from .models import HealthRecord
from .serializers import HealthRecordSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class HealthRecordViewSet(viewsets.ModelViewSet):
    serializer_class = HealthRecordSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username is not None:
            return HealthRecord.objects.filter(username=username)
        return HealthRecord.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, *args, **kwargs):
        queryset = HealthRecord.objects.all()
        record_id = self.kwargs.get('pk')
        record = get_object_or_404(queryset, pk=record_id)
        serializer = HealthRecordSerializer(record)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        queryset = HealthRecord.objects.all()
        record_id = self.kwargs.get('pk')
        record = get_object_or_404(queryset, pk=record_id)
        serializer = HealthRecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, *args, **kwargs):
        queryset = HealthRecord.objects.all()
        record_id = self.kwargs.get('pk')
        record = get_object_or_404(queryset, pk=record_id)
        record.delete()
        return Response(status=204)