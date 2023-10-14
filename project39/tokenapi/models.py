from django.db import models

# Create your models here.


class BikeModel(models.Model):
    name = models.CharField(max_length=100)

    def  __str__(self):
        return self.name


class BikeColor(models.Model):
    name = models.CharField(max_length=100)

    def  __str__(self):
        return self.name




class Bike(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(BikeModel,
                            related_name='BikeModel',
                            db_column='model',
                            on_delete=models.CASCADE
                            )
    colors = models.ManyToManyField(BikeColor)
    is_avalible = models.BooleanField(null=True, blank=True)

    def  __str__(self):
        return self.name


















