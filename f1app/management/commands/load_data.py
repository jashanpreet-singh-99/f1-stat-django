import json
from django.core.management.base import BaseCommand
from f1app.models import Circuit, Race, DriverStanding

class Command(BaseCommand):
    help = 'Load race data from JSON file'
    print('# \n # \n')
    def handle(self, *args, **kwargs):
        with open('../race_data_2024.json') as f:
            race_data = json.load(f)

        for race in race_data:
            circuit_data = race['location']
            circuit, created = Circuit.objects.get_or_create(
                name=race['circuitName'],
                defaults={
                    'location': circuit_data['locality'],
                    'country': circuit_data['country'],
                    'lat': circuit_data['lat'],
                    'long': circuit_data['long']
                }
            )
            race_instance, created = Race.objects.get_or_create(
                name=race['raceName'],
                circuit=circuit,
                date=race['date'],
                defaults={
                    'fastest_lap': race['fastestLap'],
                    'slowest_lap': race['slowestLap']
                }
            )
            for standing in race['driversStandings']:
                DriverStanding.objects.create(
                    race=race_instance,
                    driver_id=standing['driverId'],
                    driver_name=standing['driverName'],
                    constructor=standing['constructor'],
                    grid_position=standing['gridPosition'],
                    final_position=standing['finalPosition'],
                    status=standing['status'],
                    max_avg_speed=standing.get('maxAvgSpeed', None),
                    min_avg_speed=standing.get('minAvgSpeed', None)
                )