from django.db import models

# Create your models here.

class AbstractItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



# from .abstract_models import AbstractItem

class Book(AbstractItem):
    author = models.CharField(max_length=100)
    movies = models.ManyToManyField('Movie', related_name='books', blank=True)

    def __str__(self):
        return self.author

class Movie(AbstractItem):
    director = models.CharField(max_length=100)



    def __str__(self):
        return self.director