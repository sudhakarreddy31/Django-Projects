from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False,blank=True,null=True)


    def __str__(self):
        return self.task_name