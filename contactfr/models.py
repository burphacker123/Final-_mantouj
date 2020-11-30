from django.db import models

class contact(models.Model):
    Prenom = models.CharField(max_length=50)
    Nom = models.CharField(max_length=50)
    Email = models.EmailField(     )
    Produit = models.CharField(blank=True, null=True, max_length=5000)
    Message = models.CharField(blank=True, null=True, max_length=50000)
    def __str__(self):
        return f'{self.Prenom} {self.Nom}'
