from django.db import models

# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    attendees = models.IntegerField()

    def __str__(self):
        return self.name

