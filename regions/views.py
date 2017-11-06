from django.template import  RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def regions(request):
	return render(request,"regions/regions.html")
		

def manualActualization(request):
	return HttpResponse("Ręczna aktualizacja stanu dróg")
	

def actualUpdates(request):
	return HttpResponse("Wyświetl aktualnie przeprowadzane aktualizacje")
	
	
def updatesHistory(request):
	return HttpResponse("Historia aktualizacji")