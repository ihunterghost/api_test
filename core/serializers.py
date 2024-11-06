from rest_framework import serializers
from .models import *

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['mac', 'sensor']

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['mac', 'part', 'zone', 'url', 'date', 'id_event']
        
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['mac', 'type', 'location']

class CondominiumSerializer(serializers.ModelSerializer):

    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Condominium
        fields = ['id', 'name', 'description', 'devices']