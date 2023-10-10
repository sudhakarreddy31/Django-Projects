from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name
    







