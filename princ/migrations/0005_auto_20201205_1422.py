# Generated by Django 3.1.2 on 2020-12-05 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('princ', '0004_auto_20201120_1347'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutPage',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.RemoveField(
            model_name='homeproducts',
            name='Artisanal',
        ),
        migrations.RemoveField(
            model_name='homeproducts',
            name='Natural',
        ),
        migrations.DeleteModel(
            name='ArtisanalProduct',
        ),
        migrations.DeleteModel(
            name='HomeProducts',
        ),
        migrations.DeleteModel(
            name='NaturalProduct',
        ),
    ]
