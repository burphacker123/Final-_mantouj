from django.db import models

# Create your models here.
class HomeSliders(models.Model):
    image = models.ImageField(upload_to='pics')
class NaturalProduct(models.Model):
    name = models.CharField(max_length=50000)
    price = models.DecimalField(decimal_places=3, max_digits=6)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(max_length=10000000)
class NaturalProduct(models.Model):
    name = models.CharField(max_length=50000)
    price = models.DecimalField(decimal_places=3, max_digits=6)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(max_length=10000000)
class ArtisanalProduct(models.Model):
    name = models.CharField(max_length=50000)
    price = models.DecimalField(decimal_places=3, max_digits=6)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(max_length=10000000)
class HomeProducts(models.Model):
    Natural = models.ManyToManyField(NaturalProduct)
    Artisanal = models.ManyToManyField(ArtisanalProduct)
class AboutPage(models.Model):
    Title = models.CharField(max_length=5000000)
    body = models.TextField(max_length=1002335489)
    image = models.ImageField(upload_to='pics')