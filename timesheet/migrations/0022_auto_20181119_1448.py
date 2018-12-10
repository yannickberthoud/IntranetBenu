# Generated by Django 2.1.3 on 2018-11-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0021_auto_20181119_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timesheet',
            old_name='end_time',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='timesheet',
            old_name='start_time',
            new_name='start',
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='allDay',
            field=models.BooleanField(blank=True, default=False, help_text="If it's a full day work, just click 'Now' for start/end", verbose_name='All day'),
        ),
    ]