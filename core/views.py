from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    
class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    
class CondominiumViewSet(viewsets.ModelViewSet):
    queryset = Condominium.objects.all()
    serializer_class = CondominiumSerializer