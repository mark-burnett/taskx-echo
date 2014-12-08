from . import models
from celery import current_app
from django.db.models.signals import post_save


def trigger_webhooks(instance, created, **kwargs):
    if instance.subscribedURL:
        current_app.tasks['webhook'].delay(instance.subscribedURL, {
            'outputs': instance.inputs,
            'status': instance.status,
        })


post_save.connect(trigger_webhooks, sender=models.Task,
                  dispatch_uid='trigger-webhooks')
