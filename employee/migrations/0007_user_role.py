# Generated by Django 2.1.3 on 2018-11-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20181122_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('E', 'Employee'), ('R', 'Responsable'), ('D', 'Director')], default='E', max_length=1, verbose_name='Role'),
            preserve_default=False,
        ),
    ]
