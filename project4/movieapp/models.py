from django.db import models

# Create your models here.



class Movie(models.Model):
    movie_title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    actor_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)


    def __str__(self):
        return self.movie_title