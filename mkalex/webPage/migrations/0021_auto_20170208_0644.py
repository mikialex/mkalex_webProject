# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0020_article_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
