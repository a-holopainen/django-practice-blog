# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Problem',
        ),
    ]
