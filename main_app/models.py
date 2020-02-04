from django.db import models

# Create your models here.
class Pop(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.IntegerField()

    def __str__(self):
        return self.name
