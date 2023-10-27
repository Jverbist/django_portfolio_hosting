from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200) 
    date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
            return self.title

