# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-07 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180807_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='abc', unique=True),
        ),
    ]