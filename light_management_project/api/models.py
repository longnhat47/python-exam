from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Home(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Light(models.Model):
    id = models.IntegerField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    brightness = models.IntegerField()
    status = models.CharField(max_length=10, default='off')

class LightStatusHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    light = models.ForeignKey(Light, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10)