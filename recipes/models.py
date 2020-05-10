from django.db import models

class recipe(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 60)
    
