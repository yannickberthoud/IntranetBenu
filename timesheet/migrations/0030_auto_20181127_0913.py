# Generated by Django 2.1.3 on 2018-11-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0029_auto_20181126_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='date',
            field=models.DateField(),
        ),
    ]