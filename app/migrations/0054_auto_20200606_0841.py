# Generated by Django 2.2.4 on 2020-06-06 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_auto_20200507_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointsort',
            name='analog',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pointsort',
            name='grammar',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pointsort',
            name='math1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pointsort',
            name='math2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pointsort',
            name='understand',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
