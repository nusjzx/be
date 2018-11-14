# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-11 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('organisation', models.CharField(max_length=50)),
                ('webpage', models.CharField(max_length=50)),
                ('corresponding', models.CharField(max_length=50)),
                ('person_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('submission_no', models.IntegerField(primary_key=True, serialize=False)),
                ('track_no', models.IntegerField()),
                ('track_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=50)),
                ('submitted', models.CharField(max_length=50)),
                ('last_updated', models.CharField(max_length=50)),
                ('form_fields', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=50)),
                ('decision', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='submission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Submission'),
        ),
    ]