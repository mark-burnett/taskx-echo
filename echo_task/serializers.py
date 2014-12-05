from . import models
from .fields import PassThroughField
from rest_framework import serializers

__all__ = ['TaskSerializer']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    inputs = PassThroughField()
    outputs = serializers.ReadOnlyField(source='inputs')

    class Meta:
        model = models.Task
        fields = ('url', 'inputs', 'outputs')
