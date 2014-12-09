from . import models
from django.db.models.signals import post_save


def trigger_webhooks(instance, created, **kwargs):
    instance.succeed()


post_save.connect(trigger_webhooks, sender=models.Task,
                  dispatch_uid='trigger-webhooks')
