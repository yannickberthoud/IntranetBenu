# Generated by Django 2.1.3 on 2018-11-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_auto_20181115_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='current_year',
            field=models.PositiveSmallIntegerField(default=2018),
            preserve_default=False,
        ),
    ]
