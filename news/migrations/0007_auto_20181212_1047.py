# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-12 07:47
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20181212_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]
