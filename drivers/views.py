from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def drivers(request):
    return HttpResponse("Driver List")
