from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Car
from .forms import CarForm

class CarListView(LoginRequiredMixin, generic.ListView):
    template_name = 'cars/car_list_final.html'
    context_object_name = 'all_cars'

    def get_queryset(self):
        return Car.objects.all()

class CarCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CarForm
    model = Car
    template_name_suffix = '_create_form'
    success_url ='/car_list/'

class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = '__all__'
    template_name_suffix = '_update_form'

class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    fields = '__all__'
    template_name_suffix = '_delete_form'
