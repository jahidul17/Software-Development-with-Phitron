# Generated by Django 5.1 on 2024-12-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_account_on_userbankaccount_account_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_type',
            field=models.CharField(choices=[('Savings', 'Savings'), ('Current', 'Current')], max_length=10),
        ),
    ]