# Generated by Django 3.1.2 on 2020-11-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20201128_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
