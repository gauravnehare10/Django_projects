from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class ActivityLog(models.Model):
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.action} at {self.timestamp}'
    
    