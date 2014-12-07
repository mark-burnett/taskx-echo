from . import models
from .fields import PassThroughField
from rest_framework import serializers

__all__ = ['TaskSerializer']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    inputs = PassThroughField()
    outputs = serializers.ReadOnlyField(source='inputs')
    subscribedURL = serializers.URLField(required=False)
    status = serializers.CharField(required=False)

    class Meta:
        model = models.Task
        fields = ('url', 'inputs', 'outputs', 'status', 'subscribedURL')
