from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/username_userid/<filename>
    return '{0}_{1}/{2}'.format("HealthRecords", instance.username, filename)

class HealthRecord(models.Model):
    username = models.CharField(max_length=255)
    email_id = models.EmailField()
    record_details = models.TextField()
    file = models.FileField(upload_to=user_directory_path)
    
    
    
# from django.db import models
# from hashlib import sha256

# class MedicalRecord(models.Model):
#     username = models.CharField(max_length=255)
#     email_id = models.EmailField()
#     record_details = models.TextField()
#     file = models.FileField(upload_to=user_directory_path)
#     previous_hash = models.CharField(max_length=64, blank=True)
#     hash = models.CharField(max_length=64, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.previous_hash:
#             last_record = MedicalRecord.objects.order_by('-id').first()
#             self.previous_hash = last_record.hash if last_record else ''
#         self.hash = self.calculate_hash()
#         super().save(*args, **kwargs)

#     def calculate_hash(self):
#         data = f'{self.username}{self.email_id}{self.record_details}{self.file}{self.previous_hash}'
        # return sha256(data.encode('utf-8')).hexdigest()