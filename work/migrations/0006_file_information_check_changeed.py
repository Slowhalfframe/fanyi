# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-19 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_file_information_jindu'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_information',
            name='check_changeed',
            field=models.IntegerField(default=0, verbose_name='是否修改过'),
        ),
    ]
