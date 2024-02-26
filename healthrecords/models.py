from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/username_userid/<filename>
    return '{0}_{1}/{2}'.format("HealthRecords", instance.username, filename)

class HealthRecord(models.Model):
    username = models.CharField(max_length=255)
    email_id = models.EmailField()
    record_details = models.TextField()
    file = models.FileField(upload_to=user_directory_path)