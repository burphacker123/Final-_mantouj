# Generated by Django 3.1.2 on 2020-11-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('princ', '0002_auto_20200913_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('Title', models.CharField(max_length=5000)),
                ('body', models.TextField(max_length=10020)),
            ],
        ),
    ]