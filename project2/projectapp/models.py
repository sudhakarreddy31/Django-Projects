from django.db import models
from django.urls import reverse

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ceo = models.CharField(max_length=255)
    number = models.IntegerField()



    def  get_absolute_url (self):
        return reverse('detailview',kwargs={'pk':self.pk})
    