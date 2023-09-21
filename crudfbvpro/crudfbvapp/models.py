from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=255)
    esal= models.FloatField(max_length=20)
    eaddr = models.CharField(max_length=255)

    

