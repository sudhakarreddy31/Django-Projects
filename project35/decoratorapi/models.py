from django.db import models

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_college = models.CharField(max_length=100)
    student_branch = models.ManyToManyField(Branch)

    def __str__(self):
        return self.student_name
    



















