from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.fullname #+ '' + self.emp_code + self.mobile
    