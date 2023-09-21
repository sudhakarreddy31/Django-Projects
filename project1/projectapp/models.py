from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()
    price = models.FloatField()

    
    def  get_absolute_url (self):
        return reverse('details',kwargs={'pk':self.pk})
    
