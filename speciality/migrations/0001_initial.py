# Generated by Django 5.0.2 on 2024-05-12 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.TextField(verbose_name='Факультет')),
                ('color', models.CharField(max_length=6, verbose_name='Цвет тикера (HEX)')),
                ('code', models.CharField(max_length=255, verbose_name='Код направления')),
                ('name', models.TextField(verbose_name='Название направления')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality.speciality', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
    ]
