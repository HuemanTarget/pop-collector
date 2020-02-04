from djmoney.models.fields import MoneyField
from django.db import models
from django.urls import reverse

# Create your models here.
class Pop(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pop_id': self.id})
