# Generated by Django 2.2.4 on 2019-10-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_news_ort_ortdesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='lang',
            field=models.IntegerField(blank=True, choices=[(1, 'KG'), (2, 'RU')], null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='lang',
            field=models.IntegerField(blank=True, choices=[(1, 'KG'), (2, 'RU')], null=True),
        ),
    ]
