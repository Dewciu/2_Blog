# Generated by Django 4.0.1 on 2022-02-12 18:16

import datetime
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=5000)),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='blogposts\\media\\photos'), upload_to='')),
                ('date_of_publication', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 2, 12, 19, 16, 13, 993061))),
                ('language', models.CharField(choices=[('PL', 'Polski'), ('EN', 'English'), ('DE', 'Deutsch')], default='PL', max_length=2)),
            ],
        ),
    ]
