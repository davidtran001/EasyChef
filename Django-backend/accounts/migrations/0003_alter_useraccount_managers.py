# Generated by Django 4.1.6 on 2023-03-14 00:23

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_useraccount_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='useraccount',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
