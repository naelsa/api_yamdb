# Generated by Django 2.2.16 on 2022-07-17 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220715_0836'),
        ('titles', '0004_auto_20220716_1631'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Titles',
            new_name='Title',
        ),
    ]
