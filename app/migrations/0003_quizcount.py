# Generated by Django 2.2.4 on 2019-10-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190930_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('true_quiz', models.IntegerField()),
                ('false_quiz', models.IntegerField()),
            ],
        ),
    ]
