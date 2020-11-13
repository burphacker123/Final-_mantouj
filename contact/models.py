from django.db import models

class contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    product = models.TextField(blank=True, null=True, max_length=5000)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
