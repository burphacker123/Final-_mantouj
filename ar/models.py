from django.db import models

# Create your models here.
class HomeSliders(models.Model):
    image = models.ImageField(upload_to='pics')
    def __str__(self):
        return f'{self.image}'
