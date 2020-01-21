# Generated by Django 2.2.4 on 2020-01-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20200120_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likequiz',
            name='is_like',
        ),
        migrations.AddField(
            model_name='likequiz',
            name='like',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Like'), (2, 'UnLike')], null=True),
        ),
    ]
