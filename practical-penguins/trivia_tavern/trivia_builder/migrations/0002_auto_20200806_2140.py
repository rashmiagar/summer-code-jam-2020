# Generated by Django 3.0.8 on 2020-08-07 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_builder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triviaquestion',
            name='question_type',
        ),
        migrations.AddField(
            model_name='triviaquestion',
            name='question_index',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
