from django.db import models
from artisanalProd.models import ArtisanalProd
from naturalProd.models import NaturalProd
class HomeObj(models.Model):
    nature = models.ManyToManyField(NaturalProd)
    artisanal = models.ManyToManyField(ArtisanalProd)
