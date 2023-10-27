from django.db import models
from django.db.models.fields import CharField

# Create your models here.
# After you make a model type in the terminal python manage.py makemigrations -> python manage.py migrate
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

