# Generated by Django 3.2.7 on 2021-09-25 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postmodel_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка'),
        ),
    ]
