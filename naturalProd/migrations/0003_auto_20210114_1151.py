# Generated by Django 3.1.4 on 2021-01-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naturalProd', '0002_naturalprod_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='naturalprod',
            name='pricedemikg',
            field=models.FloatField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='naturalprod',
            name='pricequartkg',
            field=models.FloatField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
