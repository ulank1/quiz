# Generated by Django 2.2.4 on 2020-06-07 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_pointsort_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.IntegerField(blank=True, choices=[(1, 'KG'), (2, 'RU')], null=True)),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Информация об Оплате',
                'verbose_name_plural': 'Информации об Оплате',
            },
        ),
    ]