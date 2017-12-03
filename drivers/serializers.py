from rest_framework import serializers

from drivers.models import Driver
from regions.serializers import RegionSerializer


class DriverSerializer(serializers.ModelSerializer):

    schedule = RegionSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ('full_name', 'gender', 'schedule')
