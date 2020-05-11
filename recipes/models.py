from django.db import models
from django.contrib.postgres.fields import ArrayField

class recipe(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    duration = models.CharField(max_length = 6)

    ingredients = models.TextField()
    introduction = models.TextField()
    instructionsTxt = ArrayField(models.TextField())
    # instructionsImg = ArrayField(models.ImageField(upload_to = 'images/'))


