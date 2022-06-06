# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class person(models.model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

class letter(models.model):
    author = models.IntegerField()           # author id from user table
    registration_date = model.DateField()     
    letter_number = model.CharField()
    letter_date = model.CharField()
    receiver_name = model.CharField()
    receiver_post = model.CharField()
    welcom = model.CharField()
    letter_text = model.TextField()
    Signatory_id = model.CharField()        # get from user table
             