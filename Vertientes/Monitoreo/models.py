from django.db import models

# Create your models here.

class ArduinoData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
    