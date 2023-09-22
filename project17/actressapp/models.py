from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Actress(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    actresses = models.ManyToManyField(Actress, related_name='movies')

    def __str__(self):
        return self.title