from django.db import models

class recipe(models.Model):
    recipe_image = models.ImageField(upload_to = 'images/')
    recipe_name = models.CharField(max_length = 20)
    
