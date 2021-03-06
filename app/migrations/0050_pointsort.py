# Generated by Django 2.2.4 on 2020-04-12 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_analogort_categoryort_grammarort_math1ort_math2ort_payort_understandort'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointsOrt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('point', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ort', to='app.Users')),
            ],
            options={
                'verbose_name': 'Название пробного теста',
                'verbose_name_plural': 'Названии пробного теста',
            },
        ),
    ]
