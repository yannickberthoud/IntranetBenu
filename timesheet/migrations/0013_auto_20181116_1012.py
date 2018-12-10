# Generated by Django 2.1.3 on 2018-11-16 09:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timesheet', '0012_auto_20181115_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workbench',
            name='timesheet',
        ),
        migrations.RemoveField(
            model_name='expansereport',
            name='timesheet',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='current_week',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='current_year',
        ),
        migrations.AddField(
            model_name='expansereport',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesheet',
            name='category',
            field=models.CharField(choices=[('C', 'Central work'), ('J', 'Justified absence'), ('T', 'Travel'), ('V', 'Vacation')], default='C', max_length=1, verbose_name='Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesheet',
            name='comment',
            field=models.CharField(default='', max_length=64, verbose_name='Comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesheet',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 11, 16, 10, 11, 36, 224010)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesheet',
            name='duration_work',
            field=models.TimeField(default='08:30:00', verbose_name='Duration work'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesheet',
            name='is_all_day_work',
            field=models.BooleanField(blank=True, default=False, verbose_name='All day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesheet',
            name='title',
            field=models.CharField(default='test', max_length=64, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Workbench',
        ),
    ]
