# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_userprofile_forwardedmail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='shadowExpire',
        ),
    ]