# Generated by Django 3.1.2 on 2020-11-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('princ', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Imgheight',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='Imgwidth',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
