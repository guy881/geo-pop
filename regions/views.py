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

class RegionsView(TemplateView):
    template_name = "regions/regions.html"

    def get(self, request):
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

class AddDriverToRegionView(TemplateView):
    template_name = "regions/add_driver_to_region.html"
     
    def get_queryset(self, request):
        drivers = Driver.objects.all()
        return drivers
		
        
def manualActualization(request):
	return HttpResponse("Ręczna aktualizacja stanu dróg")
	

def actualUpdates(request):
	return HttpResponse("Wyświetl aktualnie przeprowadzane aktualizacje")
	
	
def updatesHistory(request):
	return HttpResponse("Historia aktualizacji")