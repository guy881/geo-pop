from django.template import  RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import GeoLocalization, Region
from drivers.models import Driver

class RegionsView(TemplateView):
    template_name = "regions/regions.html"
    
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