# Generated by Django 3.1.2 on 2020-11-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='product',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]