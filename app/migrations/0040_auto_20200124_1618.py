# Generated by Django 2.2.4 on 2020-01-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20200120_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='answertocomment',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='commentquestion',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
