# Generated by Django 2.1.3 on 2018-11-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0022_auto_20181119_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='end',
            field=models.DateTimeField(verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='start',
            field=models.DateTimeField(verbose_name='Start time'),
        ),
    ]
