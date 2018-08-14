from django.db import models

# Create your models here.
class Project(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=20)