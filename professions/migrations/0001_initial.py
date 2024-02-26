# Generated by Django 5.0.2 on 2024-02-23 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=255)),
                ('pointers', models.IntegerField(default=3)),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professions.professions')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='card_images/')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professions.professions')),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='promo_images/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professions.professions')),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_degree', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
                ('budget_places_count', models.IntegerField()),
                ('passing_score', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('period', models.IntegerField()),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professions.professions')),
            ],
        ),
    ]