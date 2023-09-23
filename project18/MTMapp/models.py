from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    established_date = models.DateField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
