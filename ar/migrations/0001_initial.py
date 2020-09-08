# Generated by Django 3.0.8 on 2020-09-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=5000000)),
                ('body', models.TextField(max_length=1002335489)),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='ArtisanalProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50000)),
                ('price', models.DecimalField(decimal_places=3, max_digits=4)),
                ('image', models.ImageField(upload_to='pics')),
                ('description', models.TextField(max_length=10000000)),
            ],
        ),
        migrations.CreateModel(
            name='HomeSliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='NaturalProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50000)),
                ('price', models.DecimalField(decimal_places=3, max_digits=4)),
                ('image', models.ImageField(upload_to='pics')),
                ('description', models.TextField(max_length=10000000)),
            ],
        ),
        migrations.CreateModel(
            name='HomeProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Artisanal', models.ManyToManyField(to='ar.ArtisanalProduct')),
                ('Natural', models.ManyToManyField(to='ar.NaturalProduct')),
            ],
        ),
    ]
