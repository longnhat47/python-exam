from rest_framework import serializers
from .models import Light, Room

class LightCalculateSerializer(serializers.Serializer):
    light_brightness_list = serializers.ListField(child=serializers.IntegerField())
    expected_brightness = serializers.IntegerField()

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = ['id', 'name', 'color', 'brightness', 'status']

class RoomLightsSerializer(serializers.ModelSerializer):
    lights = LightSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'lights']