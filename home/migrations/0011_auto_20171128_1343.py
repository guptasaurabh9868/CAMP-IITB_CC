# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20171128_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='shadowExpire',
            field=models.IntegerField(),
        ),
    ]
