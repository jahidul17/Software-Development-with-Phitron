# Generated by Django 5.1 on 2024-12-15 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_brand'),
        ('posts', '0002_remove_post_category_remove_post_title_post_brand_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]