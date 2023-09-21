# ormsapp/models.py
from django.db import models

class Employee(models.Model):
    emp_number = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    emp_location = models.CharField(max_length=100)
    emp_salary = models.FloatField(default=10)

    def __str__(self):
        return f'{self.emp_name} (ID: {self.emp_number})'
