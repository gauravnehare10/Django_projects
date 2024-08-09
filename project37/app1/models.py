from django.db import models

# Create your models here.
class Marks(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=100)
    python = models.FloatField()
    html = models.FloatField()
    javascript = models.FloatField()
