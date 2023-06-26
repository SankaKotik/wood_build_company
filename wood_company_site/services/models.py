from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/', null=True)