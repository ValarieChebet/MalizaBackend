# Generated by Django 5.0.4 on 2024-04-30 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_name',
        ),
    ]
