# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filed_date', models.DateTimeField(verbose_name='date filed')),
                ('agency', models.CharField(max_length=200)),
                ('submission_notes', models.TextField(verbose_name="notes about submission (did you send by mail or email? did they tell you what track it's on?)")),
                ('received_ack_letter', models.BooleanField(verbose_name='Have you received an acknowledgement letter yet?')),
                ('ack_date', models.DateTimeField(verbose_name='date acknowledgement letter received')),
                ('request_number', models.CharField(max_length=200)),
                ('received_response', models.BooleanField(verbose_name='Have you received responsive docs (or a denial) yet?')),
                ('resp_date', models.DateTimeField(verbose_name='date response received')),
                ('response_notes', models.TextField(verbose_name='Notes about your response. (complain about redactions here!) ')),
                ('response_url', models.TextField(verbose_name='URL of docs (if they were given to you via a web link)')),
                ('appealed', models.BooleanField(verbose_name='Have you (or the lawyers) appealed this?')),
                ('appeal_date', models.DateTimeField(verbose_name='date appeal filed')),
            ],
        ),
        migrations.CreateModel(
            name='HumanBeing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='foia',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foias.HumanBeing'),
        ),
    ]
