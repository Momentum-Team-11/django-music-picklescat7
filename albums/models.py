from django.db import models
from django.db import (models)
from django.utils import timezone
# from datetime import datetime

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def add_new(self):
        self.created_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    
    
# Album: title, artist, created_date, comments (maybe)
# need a publish model - "add_new"