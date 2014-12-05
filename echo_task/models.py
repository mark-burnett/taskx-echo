from django.db import models
from django_pgjson.fields import JsonField

__all__ = ['Task']


class Task(models.Model):
    inputs = JsonField()
