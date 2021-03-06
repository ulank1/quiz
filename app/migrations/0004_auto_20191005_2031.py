# Generated by Django 2.2.4 on 2019-10-05 14:31

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_quizcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=app.models.image_upload_to, verbose_name='логотип'),
        ),
        migrations.CreateModel(
            name='UniversitySubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.IntegerField(blank=True, choices=[(1, 'KG'), (2, 'RU')], null=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('desc', models.CharField(max_length=1000, verbose_name='Информация')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='app.University', verbose_name='Универ')),
            ],
            options={
                'verbose_name': 'описание',
                'verbose_name_plural': 'описание',
            },
        ),
    ]
