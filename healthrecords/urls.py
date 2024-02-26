from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import HealthRecordViewSet 


router = DefaultRouter()
router.register(r'healthrecords', HealthRecordViewSet, basename='healthrecord')

urlpatterns = [
    path('', include(router.urls)),
]



