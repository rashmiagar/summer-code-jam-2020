# Generated by Django 3.0.9 on 2020-08-09 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifapp', '0010_auto_20200809_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_id',
        ),
    ]
