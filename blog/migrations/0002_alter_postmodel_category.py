# Generated by Django 3.2.7 on 2021-09-26 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postmodel",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="blog.category", verbose_name="Категория"
            ),
        ),
    ]
