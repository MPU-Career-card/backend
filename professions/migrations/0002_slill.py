# Generated by Django 5.0.2 on 2024-04-12 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название навыка')),
                ('description', models.TextField(verbose_name='Описание навыка')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professions.professions', verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
    ]
