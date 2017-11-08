from django.template import  RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class RegionsView(TemplateView):
    template_name = "regions/regions.html"
    
class AddDriverToRegionView(TemplateView):
    template_name = "regions/add_driver_to_region.html"
		

def manualActualization(request):
	return HttpResponse("Ręczna aktualizacja stanu dróg")
	

def actualUpdates(request):
	return HttpResponse("Wyświetl aktualnie przeprowadzane aktualizacje")
	
	
def updatesHistory(request):
	return HttpResponse("Historia aktualizacji")