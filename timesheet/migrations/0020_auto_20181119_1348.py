# Generated by Django 2.1.3 on 2018-11-19 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0019_auto_20181119_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='start_time',
        ),
    ]
