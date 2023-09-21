from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Writer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Songs(models.Model):
    song_name = models.CharField(max_length=100)
    song_duration = models.FloatField()
    song_writer = models.ForeignKey(Writer, on_delete=models.CASCADE)


    def __str__(self):
        return self.song_name



class Reader(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Story(models.Model):
    name = models.CharField(max_length=100)
    duration = models.FloatField()
    reader = models.ManyToManyField(Reader)


    def __str__(self):
        return self.name

