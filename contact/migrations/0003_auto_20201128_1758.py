# Generated by Django 3.1.2 on 2020-11-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20201117_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]