from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=8)

    def __str__(self):
        return self.name



class Store(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)


    def __str__(self):
        return self.name
