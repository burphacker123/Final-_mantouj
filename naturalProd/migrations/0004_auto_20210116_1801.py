# Generated by Django 3.0 on 2021-01-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naturalProd', '0003_auto_20210114_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naturalprod',
            name='ARdescription',
            field=models.TextField(max_length=12000),
        ),
        migrations.AlterField(
            model_name='naturalprod',
            name='ENdescription',
            field=models.TextField(max_length=12000),
        ),
        migrations.AlterField(
            model_name='naturalprod',
            name='FRdescription',
            field=models.TextField(max_length=12000),
        ),
    ]
