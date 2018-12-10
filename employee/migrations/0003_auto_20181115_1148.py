# Generated by Django 2.1.3 on 2018-11-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20181115_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Yannick', max_length=64, verbose_name='Firstname'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Berthoud', max_length=64, verbose_name='Lastname'),
            preserve_default=False,
        ),
    ]