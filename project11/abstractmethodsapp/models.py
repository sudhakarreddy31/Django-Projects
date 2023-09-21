from django.db import models

# Create your models here

class CommonFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class Post(CommonFields):
    title = models.CharField(max_length=100)
    content = models.TextField()
    

    def __str__(self):
        return self.title





























