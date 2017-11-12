from django.template import  RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import GeoLocalization, Region
from django.utils import timezone
from drivers.models import Driver
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class RegionsView(LoginRequiredMixin, TemplateView):
    template_name = "regions/regions.html"

    def get(self, request):
        GeoLocalization.objects.all().delete()
        Region.objects.all().delete()
        lat = [52.3500, 52.2771, 52.1870, 52.0962]
        lon = [20.7810, 20.8678, 20.9573, 21.0475, 21.1374, 21.2271]
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[0], longitude=lon[0]),
                              south_east=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[1]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[0], longitude=lon[1]),
                              south_east=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[2]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[0], longitude=lon[2]),
                              south_east=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[3]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[0], longitude=lon[3]),
                              south_east=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[4]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[0], longitude=lon[4]),
                              south_east=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[5]))

        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[0]),
                              south_east=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[1]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[1]),
                              south_east=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[2]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[2]),
                              south_east=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[3]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[3]),
                              south_east=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[4]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[1], longitude=lon[4]),
                              south_east=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[5]))

        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[0]),
                              south_east=GeoLocalization.objects.create(latitude=lat[3], longitude=lon[1]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[1]),
                              south_east=GeoLocalization.objects.create(latitude=lat[3], longitude=lon[2]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[2]),
                              south_east=GeoLocalization.objects.create(latitude=lat[3], longitude=lon[3]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[3]),
                              south_east=GeoLocalization.objects.create(latitude=lat[3], longitude=lon[4]))
        Region.objects.create(is_updated=True, last_updated=timezone.now(),
                              north_west=GeoLocalization.objects.create(latitude=lat[2], longitude=lon[4]),
                              south_east=GeoLocalization.objects.create(latitude=lat[3], longitude=lon[5]))
        regions = Region.objects.all()
        nlat=[]
        nlon=[]
        slat = []
        slon = []
        for i in range (0, regions.count()) :
            nlat.append(float(regions.select_related('north_west__latitude').values_list('north_west__latitude')[i][0]))
            nlon.append(float(regions.select_related('north_west__longitude').values_list('north_west__longitude')[i][0]))
            slat.append(float(regions.select_related('south_east__latitude').values_list('south_east__latitude')[i][0]))
            slon.append(float(regions.select_related('south_east__longitude').values_list('south_east__longitude')[i][0]))
        return render(request, 'regions/regions.html', {"nlat": nlat, "nlon": nlon, "slat":slat, "slon":slon})

class AddDriverToRegionView(LoginRequiredMixin, TemplateView):
    template_name = "regions/add_driver_to_region.html"
     
    def get_queryset(self, request):
        drivers = Driver.objects.all()
        return drivers
		
        
#def manualActualization(request):
#	return HttpResponse("Ręczna aktualizacja stanu dróg")
#	
#
#def actualUpdates(request):
#	return HttpResponse("Wyświetl aktualnie przeprowadzane aktualizacje")
#	
#	
#def updatesHistory(request):
#	return HttpResponse("Historia aktualizacji")