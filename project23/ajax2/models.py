from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    dept = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    