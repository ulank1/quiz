# Generated by Django 2.2.4 on 2019-11-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20191116_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyNotif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Информация')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.AlterModelOptions(
            name='gamequizgame',
            options={},
        ),
    ]