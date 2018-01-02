from rest_framework import serializers

from regions.models import Region, GeoLocalization


class GeoLocalizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoLocalization
        fields = ('latitude', 'longitude',)
        depth = 1


class RegionSerializer(serializers.ModelSerializer):
    south_east = GeoLocalizationSerializer()#source='geoLocalization_set'
    north_west = GeoLocalizationSerializer()

    class Meta:
        model = Region
        fields = ('is_updated', 'last_updated', 'south_east', 'north_west')
        depth = 3
