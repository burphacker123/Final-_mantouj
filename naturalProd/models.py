from django.db import models

# Create your models here.
class NaturalProd(models.Model):
    ENtitle = models.CharField(max_length=200)
    FRtitle = models.CharField(max_length=200)
    ARtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    ENdescription = models.TextField(max_length=12000)
    FRdescription = models.TextField(max_length=12000)
    ARdescription = models.TextField(max_length=12000)
    pricedemikg = models.FloatField(max_length=1000)
    pricequartkg = models.FloatField(max_length=1000)
    price = models.FloatField(max_length=1000)
    pricedemikg = models.FloatField(max_length=1000)
    pricequartkg = models.FloatField(max_length=1000)
    slug = models.SlugField(unique=True)
    available = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.ENtitle}'