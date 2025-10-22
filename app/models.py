from django.db import models

class MyMusic(models.Model):
    music_name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)