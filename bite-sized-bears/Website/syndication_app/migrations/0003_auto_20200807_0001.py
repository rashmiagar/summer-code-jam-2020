# Generated by Django 3.0.7 on 2020-08-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syndication_app', '0002_auto_20200806_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]