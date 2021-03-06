# Generated by Django 2.2.4 on 2020-01-19 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_quote_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayquiz',
            name='answer_a',
        ),
        migrations.RemoveField(
            model_name='dayquiz',
            name='answer_b',
        ),
        migrations.RemoveField(
            model_name='dayquiz',
            name='answer_c',
        ),
        migrations.RemoveField(
            model_name='dayquiz',
            name='answer_d',
        ),
        migrations.RemoveField(
            model_name='dayquiz',
            name='answer_e',
        ),
        migrations.RemoveField(
            model_name='dayquiz',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='dayquiz',
            name='true_answer',
        ),
        migrations.CreateModel(
            name='CommentQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to='app.DayQuiz')),
            ],
            options={
                'verbose_name': 'Коментарий к задаче дня',
                'verbose_name_plural': 'Коментарии к задаче дня',
            },
        ),
    ]
