# Generated by Django 2.1.3 on 2018-11-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('improvement', '0002_auto_20181123_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='improvement',
            name='advancement',
            field=models.TextField(blank=True),
        ),
    ]