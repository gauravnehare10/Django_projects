from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from app1.models import Blog, ActivityLog

@receiver(post_save, sender=Blog)
def log_blog_creation(sender, instance, created, **kwargs):
    if created:
        ActivityLog.objects.create(action=f'Blog "{instance.title}" created')

@receiver(post_delete, sender=Blog)
def log_blog_deletion(sender, instance, **kwargs):
    ActivityLog.objects.create(action=f'Blog "{instance.title}" deleted')