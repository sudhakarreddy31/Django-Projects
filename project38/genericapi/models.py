from django.db import models

# Create your models here.

class EmployeeDept(models.Model):
    employee_dept_id = models.PositiveIntegerField()
    employee_dept = models.CharField(max_length=100)

    def __str__(self):
        return self.employee_dept



class Employee(models.Model):
    employee_id = models.PositiveIntegerField()
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField()
    employee_dept = models.ForeignKey(
        EmployeeDept,
        related_name='EmployeeDept',
        db_column='employee_dept',
        on_delete=models.CASCADE
    )
    employee_location = models.CharField(max_length=100)

    def __str__(self):
        return self.employee_name
