# Generated by Django 5.0.2 on 2024-02-23 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Карточка', 'verbose_name_plural': 'Карточки'},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Контент', 'verbose_name_plural': 'Контент'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name': 'Специальность', 'verbose_name_plural': 'Специальности'},
        ),
    ]
