# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-02 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['created_on'], 'verbose_name_plural': 'accounts'},
        ),
    ]
