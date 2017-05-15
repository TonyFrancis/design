# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models.event import Event
from rest_framework import viewsets
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """Event View Set."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
