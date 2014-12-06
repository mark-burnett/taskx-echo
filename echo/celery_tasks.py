from . import models
from celery import shared_task
from celery.utils.log import get_task_logger
from django.db.models.signals import post_save
import requests


LOG = get_task_logger(__name__)


@shared_task(bind=True)
def webhook(self, url, body_data):
    response = requests.put(url, body_data,
                            headers={'Content-Type': 'application/json'})

    if int(response.status_code / 200) != 1:
        LOG.warn('Failed to deliver callback to %s', url)
        self.retry()


def trigger_webhooks(instance, created, **kwargs):
    if instance.successWebhook:
        webhook.delay(instance.successWebhook, {'outputs': instance.inputs})


post_save.connect(trigger_webhooks, sender=models.Task,
                  dispatch_uid='trigger-webhooks')
