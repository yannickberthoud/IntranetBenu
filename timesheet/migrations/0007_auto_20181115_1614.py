# Generated by Django 2.1.3 on 2018-11-15 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0006_timesheet_current_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
