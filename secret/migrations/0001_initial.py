# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 19:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=32)),
                ('secret', models.CharField(max_length=256)),
                ('expires', models.DateTimeField(default=datetime.datetime(2017, 11, 4, 19, 58, 34, 354507))),
            ],
        ),
    ]
