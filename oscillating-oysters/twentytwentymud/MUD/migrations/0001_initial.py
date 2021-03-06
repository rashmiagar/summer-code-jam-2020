# Generated by Django 3.1 on 2020-08-08 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Server', max_length=50)),
                ('room_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Room', max_length=50)),
                ('description', models.TextField(max_length=512)),
                ('command_description', models.TextField(blank=True, max_length=512)),
                ('command_keyword', models.TextField(blank=True, max_length=512)),
                ('command_response', models.TextField(blank=True, max_length=512)),
                ('secret_connection_active', models.BooleanField(default=False)),
                ('connections', models.ManyToManyField(blank=True, related_name='_room_connections_+', to='MUD.Room')),
                ('next_server_connect', models.ManyToManyField(blank=True, to='MUD.Server')),
                ('secret_room_connects', models.ManyToManyField(blank=True, related_name='_room_secret_room_connects_+', to='MUD.Room')),
                ('server', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='MUD.server')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MUD.room')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
