# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-18 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yiwen',
            name='yiwen_wait_over',
            field=models.TextField(default='', verbose_name='译文待人工编译'),
        ),
    ]
