from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Car

class CarListView(LoginRequiredMixin, generic.ListView):
    template_name = 'cars/car_list.html'
    #model = Car
    context_object_name = 'car_list'

    def get_queryset(self):
        return Car.objects.all()

class CarCreateView(CreateView):
    model = Car
    fields = ['brand', 'production_year','engine_volume','need_repair','insurance_number','is_available']
