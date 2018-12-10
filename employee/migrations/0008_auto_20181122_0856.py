# Generated by Django 2.1.3 on 2018-11-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('A', 'Pharmacy assistant'), ('D', 'Director'), ('E', 'Employee'), ('P', 'Pharmacist'), ('R', 'Responsable')], max_length=1, verbose_name='Role'),
        ),
    ]