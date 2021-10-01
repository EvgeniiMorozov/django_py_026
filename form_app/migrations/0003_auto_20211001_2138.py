# Generated by Django 3.2.7 on 2021-10-01 16:38

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0002_auto_20211001_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(code='invalid', flags=re.RegexFlag['IGNORECASE'], message='Имя|Фамилия должно начинаться с только с буквы!', regex='^[a-zа-я]')], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(code='invalid', flags=re.RegexFlag['IGNORECASE'], message='Имя|Фамилия должно начинаться с только с буквы!', regex='^[a-zа-я]')], verbose_name='Фамилия'),
        ),
    ]