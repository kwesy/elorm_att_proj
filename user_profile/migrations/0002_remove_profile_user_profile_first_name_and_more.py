# Generated by Django 4.1 on 2023-08-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.TextField(default='defaults'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.TextField(default='d'),
            preserve_default=False,
        ),
    ]
