from rest_framework import serializers

from regions.models import Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('is_updated', 'last_updated', 'south_east', 'north_west')
