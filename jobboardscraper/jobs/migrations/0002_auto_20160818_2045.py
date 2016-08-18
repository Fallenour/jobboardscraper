# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
    ]