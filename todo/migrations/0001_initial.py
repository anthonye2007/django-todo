# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-21 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
