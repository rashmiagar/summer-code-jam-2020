# Generated by Django 3.0.8 on 2020-08-08 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200807_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background',
            field=models.ImageField(default='white-bg.jpg', upload_to='background'),
        ),
    ]
