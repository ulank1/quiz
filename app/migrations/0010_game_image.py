# Generated by Django 2.2.4 on 2019-10-13 08:01

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20191011_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=app.models.image_upload_to, verbose_name='картинки'),
        ),
    ]
