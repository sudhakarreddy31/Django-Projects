from django.db import models

# Create your models here.
class StrangersThings(models.Model):
    actors_name = models.CharField(max_length=100)
    actor_charactor_name= models.CharField(max_length=100)
    actress_name = models.CharField(max_length=100)
    actress_charactor_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.actors_name 

