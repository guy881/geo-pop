from django.template import  RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def regions(request):
    return render(request,"regions/regions.html")
    