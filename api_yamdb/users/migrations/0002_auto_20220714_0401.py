# Generated by Django 2.2.16 on 2022-07-14 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=50, verbose_name='Код для авторизации'),
        ),
    ]
