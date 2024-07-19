from django.db import models

# Create your models here.
class Product(models.Model):
    prodid = models.IntegerField()
    prodname = models.CharField(max_length=20)
    dateofmfg = models.DateField()
    price = models.FloatField()
