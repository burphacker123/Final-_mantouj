from django.db import models

class contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(     )
    product = models.CharField(blank=True, null=True, max_length=5000)
    message = models.CharField(blank=True, null=True, max_length=50000)
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
