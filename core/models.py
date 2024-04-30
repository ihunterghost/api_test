from django.db import models

class Log(models.Model):
    mac = models.CharField(max_length=12)
    sensor = models.IntegerField()
    message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Condominium(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Device(models.Model):
    mac = models.CharField(max_length=12, primary_key=True)
    type = models.CharField(max_length=20)
    location = models.ForeignKey(Condominium, related_name='devices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)