# Generated by Django 2.2.4 on 2019-11-01 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_maincategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='answer_a',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='ответ_а'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer_b',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='ответ_б'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer_c',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='ответ_в'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer_d',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='ответ_г'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer_e',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='ответ_д'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='вопрос'),
        ),
    ]
