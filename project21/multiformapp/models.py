from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    student_id = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    qualification = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    age = models.IntegerField()
    location = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name































