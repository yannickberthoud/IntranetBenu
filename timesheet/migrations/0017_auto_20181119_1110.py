# Generated by Django 2.1.3 on 2018-11-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0016_auto_20181119_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='end_time',
            field=models.TimeField(default='14:00'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='start_time',
            field=models.TimeField(default='12:00'),
        ),
    ]
