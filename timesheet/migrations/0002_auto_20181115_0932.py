# Generated by Django 2.1.3 on 2018-11-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workbench',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workbench',
            name='duration_work',
            field=models.TimeField(verbose_name='Duration work'),
        ),
    ]
