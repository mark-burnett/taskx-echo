from celery import current_app
from django.db import models
from django_pgjson.fields import JsonField
from django_extensions.db.fields import UUIDField
from django_fsm import FSMField, transition

__all__ = ['Task']


class Task(models.Model):

    id = UUIDField(auto=True, primary_key=True)
    inputs = JsonField(editable=False)
    state = FSMField(default='new', null=False, blank=False)
    subscribedURL = models.URLField(null=True, editable=False)

    @transition(field=state, source='new', target='succeeded')
    def succeed(self):
        if self.subscribedURL:
            current_app.tasks['webhook'].delay(self.subscribedURL, {
                'outputs': self.inputs,
                'state': self.state,
            })
