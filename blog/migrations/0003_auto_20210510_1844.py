# Generated by Django 3.1.4 on 2021-05-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210510_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogclass',
            name='image',
            field=models.ImageField(blank=True, default='#', upload_to='pics'),
        ),
    ]
