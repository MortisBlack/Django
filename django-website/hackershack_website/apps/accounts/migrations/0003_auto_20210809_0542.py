# Generated by Django 3.0.7 on 2021-08-09 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210809_0512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='interest',
            new_name='interests',
        ),
    ]
