from django.db import models

# Create your models here.

class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone
    
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
