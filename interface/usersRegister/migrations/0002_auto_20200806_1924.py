# Generated by Django 3.0.7 on 2020-08-07 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersRegister', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='users',
            name='gender',
        ),
    ]
