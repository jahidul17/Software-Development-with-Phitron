# Generated by Django 5.1 on 2025-01-06 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_moneytransfer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneytransfer',
            old_name='receive_money',
            new_name='receivemoney_account',
        ),
        migrations.RenameField(
            model_name='moneytransfer',
            old_name='send_money',
            new_name='sendmoney_account',
        ),
    ]
