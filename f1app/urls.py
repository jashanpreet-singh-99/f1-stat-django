from django.urls import path
from .views import RaceList, RaceDetail, DriverStandingList, RaceDriverStandingList, RaceConstructorFastestSpeed

urlpatterns = [
    path('races/', RaceList.as_view(), name='race-list'),
    path('races/<int:pk>/', RaceDetail.as_view(), name='race-detail'),
    path('drivers/<str:driver_id>/standings/', DriverStandingList.as_view(), name='driver-standings'),
    path('races/<int:race_id>/standings/', RaceDriverStandingList.as_view(), name='race-driver-standings'),
    path('races/<int:race_id>/constructor-fastest-speed/', RaceConstructorFastestSpeed.as_view(), name='race-constructor-fastest-speed'),
]