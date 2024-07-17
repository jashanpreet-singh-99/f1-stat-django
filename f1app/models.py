from django.db import models

class Circuit(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()

class Race(models.Model):
    name = models.CharField(max_length=100)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    date = models.DateField()
    fastest_lap = models.CharField(max_length=10, null=True)
    slowest_lap = models.CharField(max_length=10, null=True)

class DriverStanding(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver_id = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    constructor = models.CharField(max_length=100)
    grid_position = models.IntegerField()
    final_position = models.IntegerField()
    status = models.CharField(max_length=100)
    max_avg_speed = models.FloatField(null=True, blank=True)
    min_avg_speed = models.FloatField(null=True, blank=True)