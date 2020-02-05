from djmoney.models.fields import MoneyField
from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
BRANDS = (
    ('P', 'Pop!'),
    ('A', 'Action Figures'),
    ('D', 'Dorbz'),
    ('H', 'Hikari')
)


class Pop(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pop_id': self.id})
    
    def detail_entered(self):
        return self.detail_set.filter(date=date.today()).count() <= len(BRANDS)

class Detail(models.Model):
    date = models.DateField('Release Date')
    item_number = models.IntegerField()
    brand = models.CharField(
        max_length=1, 
        choices=BRANDS,
        default=BRANDS[0][0]
    )

    pop = models.ForeignKey(Pop, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_brand_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

