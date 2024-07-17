from rest_framework import serializers
from .models import Race, DriverStanding

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'

class DriverStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverStanding
        fields = '__all__'