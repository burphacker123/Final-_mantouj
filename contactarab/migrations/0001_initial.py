# Generated by Django 3.1.2 on 2020-11-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('الاسم', models.CharField(max_length=50)),
                ('اسم_العائلة', models.CharField(max_length=50)),
                ('البريد_الإلكتروني', models.EmailField(max_length=254)),
                ('المنتج', models.CharField(blank=True, max_length=5000, null=True)),
                ('رسالة', models.CharField(blank=True, max_length=50000, null=True)),
            ],
        ),
    ]
