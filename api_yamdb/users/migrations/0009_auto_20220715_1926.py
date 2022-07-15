# Generated by Django 2.2.16 on 2022-07-15 14:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_merge_20220715_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, default=uuid.UUID('2871ad15-044a-11ed-b645-18c04d9f4202'), max_length=50, verbose_name='Код для авторизации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
