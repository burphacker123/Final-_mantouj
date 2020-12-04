from django.db import models

# Create your models here.
class HomeSliders(models.Model):
    image = models.ImageField(upload_to='pics')
    def __str__(self):
        return f'{self.image}'
class NaturalProduct(models.Model):
    name = models.CharField(max_length=50000)
    price = models.DecimalField(decimal_places=3, max_digits=6)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(max_length=10000000)
    def __str__(self):
        return f'{self.name}'
class ArtisanalProduct(models.Model):
    name = models.CharField(max_length=50000)
    price = models.DecimalField(decimal_places=3, max_digits=6)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(max_length=10000000)
    def __str__(self):
        return f'{self.name}'
class HomeProducts(models.Model):
    Natural = models.ManyToManyField(NaturalProduct)
    Artisanal = models.ManyToManyField(ArtisanalProduct)
    def __str__(self):
        return f'{self.Natural.name}'
class AboutPage(models.Model):
    Title = models.CharField(max_length=5000000)
    body = models.TextField(max_length=1002335489)
    image = models.ImageField(upload_to='pics')
    def __str__(self):
        return f'{self.Title}'
class Blog(models.Model):
    image = models.ImageField(upload_to='pics')
    Title = models.CharField(max_length=5000)
    body = models.TextField(max_length=10020)
    Imgwidth = models.IntegerField()
    Imgheight = models.IntegerField()
    def __str__(self):
        return f'{self.Title}'
# Create your models here.
