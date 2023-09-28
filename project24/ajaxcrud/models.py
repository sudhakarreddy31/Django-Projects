from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    email = models.EmailField(max_length=25)
    marks = models.FloatField()

    def __str__(self):
        return self.name
    