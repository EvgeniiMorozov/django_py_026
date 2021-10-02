# Generated by Django 3.2.7 on 2021-09-26 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='Автор статьи')),
                ('title', models.CharField(max_length=50, verbose_name='Название статьи')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='URL')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('image', models.ImageField(upload_to='img', verbose_name='Картинка к посту')),
                ('publish_date', models.DateTimeField(auto_now=True, verbose_name='Время публикации')),
                ('is_published', models.BooleanField(default=True, verbose_name='Пост опубликован?')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
        ),
    ]
