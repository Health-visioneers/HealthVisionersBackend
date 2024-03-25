from django.db import models

# Create your models here.

class meetings(models.Model):
    purpose = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='meetings')
    created_for = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='meetings_for')
    created_at = models.DateTimeField(auto_now_add=True)
    meeting_id = models.IntegerField()
    def __str__(self):
        return self.title
    
