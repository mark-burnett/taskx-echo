from . import models
from taskx_service.pass_through_field import PassThroughField
from rest_framework import serializers

__all__ = ['TaskSerializer']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    inputs = PassThroughField()
    outputs = serializers.ReadOnlyField(source='inputs')
    subscribedURL = serializers.URLField(required=False)
    state = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = models.Task
        fields = ('url', 'inputs', 'outputs', 'state', 'subscribedURL')
