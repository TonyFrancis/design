from __future__ import unicode_literals

from django.db import models
from django import db
from backend.core.model import LoadByIdMixin


class Event(models.Model, LoadByIdMixin):
    """Model Event"""
    name = models.CharField(max_length=200)
