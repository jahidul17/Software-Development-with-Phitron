# Generated by Django 5.1 on 2025-01-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userbankaccount_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_type',
            field=models.CharField(choices=[('Current', 'Current'), ('Savings', 'Savings')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userbankaccount',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10),
        ),
    ]
