from django.db import models

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=24)
    bio = models.CharField(max_length=240)
    email = models.CharField(max_length=24)
    phone = models.IntegerField()

    def __str__(self):
        return self.full_name










