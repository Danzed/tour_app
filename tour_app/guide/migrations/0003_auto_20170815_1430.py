# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_auto_20170814_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_place', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tour', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Tour'),
        ),
    ]
