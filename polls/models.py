# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
  name = models.CharField(max_length = 50)
  country = models.CharField(max_length=50)
  organisation = models.CharField(max_length=50)
  webpage = models.CharField(max_length=50)
  corresponding = models.CharField(max_length=50)
  person_id = models.IntegerField(null=True)
  submission = models.ForeignKey('Submission', null=True, to_field='submission_no', on_delete=models.DO_NOTHING)

class Submission(models.Model):
  submission_no = models.IntegerField(primary_key=True)
  track_no = models.IntegerField()
  track_name = models.CharField(max_length=50)
  title = models.CharField(max_length=100)
  authors = models.CharField(max_length=50)
  submitted = models.CharField(max_length=50)
  last_updated = models.CharField(max_length=50)
  form_fields = models.CharField(max_length=50)
  keywords = models.CharField(max_length=50)
  decision = models.CharField(max_length=50)
