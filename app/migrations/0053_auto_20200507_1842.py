# Generated by Django 2.2.4 on 2020-05-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_auto_20200428_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryort',
            name='text1',
            field=models.TextField(blank=True, null=True, verbose_name='текст для чтения и понимания №1'),
        ),
        migrations.AddField(
            model_name='categoryort',
            name='text2',
            field=models.TextField(blank=True, null=True, verbose_name='текст для чтения и понимания №2'),
        ),
        migrations.AddField(
            model_name='categoryort',
            name='text3',
            field=models.TextField(blank=True, null=True, verbose_name='текст для чтения и понимания №3'),
        ),
    ]
