from django.db import models
from princ.models import ArtisanalProduct, NaturalProduct

# Create your models here.
class Cart(models.Model):
    nProduct = models.ManyToManyField(NaturalProduct, blank=True)
    aProduct = models.ManyToManyField(ArtisanalProduct, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return "Cart id: %s" %(self.id)