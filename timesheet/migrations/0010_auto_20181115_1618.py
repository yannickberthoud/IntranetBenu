# Generated by Django 2.1.3 on 2018-11-15 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0009_auto_20181115_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
