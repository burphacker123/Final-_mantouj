from django.db import models

# Create your models here.
class BlogClass(models.Model):
    ENtitle = models.CharField(max_length=200)
    FRtitle = models.CharField(max_length=200)
    ARtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics', blank=True, null=True, default='#')
    ENdescription = models.TextField(max_length=2000)
    FRdescription = models.TextField(max_length=2000)
    ARdescription = models.TextField(max_length=2000)
    imageW = models.FloatField()
    imaheH = models.FloatField()
    pdflink = models.CharField(max_length=100000000000, default="#", blank=True)
    video = models.FileField(upload_to='pics', blank=True)
    def __str__(self):
        return f'{self.ENtitle}'