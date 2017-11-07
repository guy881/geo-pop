from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Car

class CarListView(LoginRequiredMixin, generic.ListView):
    template_name = 'cars/car_list.html'
    #model = Car
    context_object_name = 'car_list'

    def get_queryset(self):
        return Car.objects.all()
