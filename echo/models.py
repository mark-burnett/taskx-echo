from django.db import models
from django_pgjson.fields import JsonField
from django_extensions.db.fields import UUIDField

__all__ = ['Task']


class Task(models.Model):

    STATUS_SUCCEEDED = 'succeeded'
    STATUS_CHOICES = (
        (STATUS_SUCCEEDED, 1),
    )

    id = UUIDField(auto=True, primary_key=True)
    inputs = JsonField()
    status = models.TextField(choices=STATUS_CHOICES, default=STATUS_SUCCEEDED)
    subscribedURL = models.URLField(null=True)
