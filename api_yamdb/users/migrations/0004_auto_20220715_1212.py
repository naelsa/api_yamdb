# Generated by Django 2.2.16 on 2022-07-15 09:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220714_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, default=uuid.UUID('33b18e3e-041e-11ed-a2fe-0871908b6167'), max_length=50, verbose_name='Код для авторизации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Админ')], default='user', max_length=13),
        ),
    ]
