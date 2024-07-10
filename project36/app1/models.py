from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField(primary_key = True)
    ename = models.CharField(max_length = 25)
    job = models.CharField(max_length=15)
    salary = models.FloatField()

    def __str__(self):
        return f"{self.empno}, {self.ename}, {self.job}, {self.salary}"