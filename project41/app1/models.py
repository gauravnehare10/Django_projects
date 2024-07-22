from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    salary = models.FloatField()
    deptno = models.ForeignKey(Dept, on_delete=models.CASCADE)
