from django.db import models

# Create your models here.

class Collage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Branch(models.Model):
    name = models.CharField(max_length=100)
    collage = models.ForeignKey(Collage,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    data_of_birth = models.DateField()
    collage = models.ForeignKey(Collage,on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
























