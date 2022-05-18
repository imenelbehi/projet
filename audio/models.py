from django.db import models

# Create your models here.
class Audio(models.Model):
    audioname = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audio')
