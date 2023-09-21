from django.db import models
from django.urls import reverse

# Create your models here.


class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def  get_absolute_url (self):
        return reverse('university-detail',kwargs={'pk':self.pk})
    

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    universities_attended = models.ManyToManyField(University, related_name='students_enrolled')
    primary_university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='primary_students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def  get_absolute_url (self):
        return reverse('student-detail',kwargs={'pk':self.pk})
    
