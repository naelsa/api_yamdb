# Generated by Django 2.2.16 on 2022-07-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0003_auto_20220714_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
    ]