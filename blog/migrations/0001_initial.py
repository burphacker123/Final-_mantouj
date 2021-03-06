# Generated by Django 3.1.4 on 2021-05-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ENtitle', models.CharField(max_length=200)),
                ('FRtitle', models.CharField(max_length=200)),
                ('ARtitle', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='pics')),
                ('ENdescription', models.TextField(max_length=2000)),
                ('FRdescription', models.TextField(max_length=2000)),
                ('ARdescription', models.TextField(max_length=2000)),
                ('imageW', models.FloatField()),
                ('imaheH', models.FloatField()),
                ('pdflink', models.CharField(blank=True, default='#', max_length=100000000000)),
            ],
        ),
    ]
