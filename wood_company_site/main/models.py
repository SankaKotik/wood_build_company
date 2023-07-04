from django.db import models


# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.type)

class PortfolioCard(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='portfolio/')
    description = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)