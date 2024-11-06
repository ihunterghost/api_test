from django.db import models
import uuid

class Log(models.Model):
    mac = models.CharField(max_length=12)
    sensor = models.IntegerField()
    message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mac = models.CharField(max_length=12)
    part = models.IntegerField()
    zone = models.IntegerField()
    url = models.CharField(max_length=150, null=True)
    date = models.DateTimeField()
    id_event = models.IntegerField()

class Condominium(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

class Device(models.Model):
    mac = models.CharField(max_length=12, primary_key=True)
    type = models.CharField(max_length=20)
    location = models.ForeignKey(Condominium, related_name='devices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)