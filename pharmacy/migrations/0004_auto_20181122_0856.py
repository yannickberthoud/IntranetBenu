# Generated by Django 2.1.3 on 2018-11-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_auto_20181122_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='uuid',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
