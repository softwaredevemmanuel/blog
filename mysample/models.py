from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    
