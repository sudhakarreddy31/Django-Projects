from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # Basic fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    age = models.IntegerField()
    date_of_birth = models.DateField()

    # Relationship fields
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    books_authored = models.ManyToManyField('Book', related_name='authors')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state}, {self.country}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
