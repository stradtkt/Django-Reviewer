# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-13 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviewers', '0002_auto_20180713_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]