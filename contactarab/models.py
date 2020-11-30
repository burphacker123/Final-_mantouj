from django.db import models

class contact(models.Model):
    الاسم  = models.CharField(max_length=50)
    اسم_العائلة = models.CharField(max_length=50)
    البريد_الإلكتروني  = models.EmailField()
    المنتج = models.CharField(blank=True, null=True, max_length=5000)
    رسالة = models.CharField(blank=True, null=True, max_length=50000)
    def __str__(self):
        return f'{self.الاسم} {self.اسم_العائلة}'
