# Generated by Django 5.1 on 2025-01-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userbankaccount_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_type',
            field=models.CharField(choices=[('Savings', 'Savings'), ('Current', 'Current')], max_length=10),
        ),
    ]
