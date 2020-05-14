from django.db import models
from django.contrib.postgres.fields import ArrayField

class recipe(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    duration = models.CharField(max_length = 6)
    mealType = models.CharField(max_length = 20)

    introduction = models.TextField()
    tools = ArrayField(models.TextField())
    prep = ArrayField(models.TextField())
    ingredients = ArrayField(models.TextField())
    ingNote = models.TextField()
    instructionsTxt = ArrayField(models.TextField())
    note = models.TextField()

