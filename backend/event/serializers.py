from .models.event import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    """
    Event serializers

    serializers
    """
    class Meta:
        model = Event
        fields = ['name', 'id']
