# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foias', '0013_auto_20170222_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='foia',
            name='request_notes',
            field=models.TextField(blank=True, verbose_name='notes about the request (did you send by mail or email? why did you phrase it the way you did?)'),
        ),
        migrations.AlterField(
            model_name='foia',
            name='request_subject',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='what was the request for?'),
        ),
        migrations.AlterField(
            model_name='foia',
            name='submission_notes',
            field=models.TextField(blank=True, verbose_name="notes about submission (did they respond by mail or email? do you have a phone number? did they tell you what track it's on?)"),
        ),
    ]
