from django.db import models

# Create your models here.
class Author(models.Model):
    authorname = models.CharField(max_length=50)

class Book(models.Model):
    bookname = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
