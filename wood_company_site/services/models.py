from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/', null=True)
    time = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)