from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Race, DriverStanding
from .serializers import RaceSerializer, DriverStandingSerializer

class RaceList(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RaceDetail(generics.RetrieveAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class DriverStandingList(generics.ListAPIView):
    serializer_class = DriverStandingSerializer

    def get_queryset(self):
        driver_id = self.kwargs['driver_id']
        return DriverStanding.objects.filter(driver_id=driver_id)

class RaceDriverStandingList(generics.ListAPIView):
    serializer_class = DriverStandingSerializer

    def get_queryset(self):
        race_id = self.kwargs['race_id']
        return DriverStanding.objects.filter(race_id=race_id)

class RaceConstructorFastestSpeed(generics.ListAPIView):
    def get(self, request, race_id):
        race = get_object_or_404(Race, pk=race_id)
        standings = DriverStanding.objects.filter(race=race)
        
        constructor_speeds = {}
        for standing in standings:
            constructor = standing.constructor
            if constructor not in constructor_speeds:
                constructor_speeds[constructor] = standing.max_avg_speed
            else:
                constructor_speeds[constructor] = max(constructor_speeds[constructor], standing.max_avg_speed)

        return Response(constructor_speeds)