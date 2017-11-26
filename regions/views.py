from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Region
from drivers.models import Driver
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



class RegionsView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = "regions/regions.html"
    context_object_name = 'all_regions'

    def get_context_data(self, **kwargs):
        context = super(RegionsView, self).get_context_data(**kwargs)
        context['all_regions'] = Region.objects.values('id', 'is_updated', 'north_west__latitude', 'north_west__longitude', 'south_east__latitude', 'south_east__longitude')
        return context

    def post(self, request, *args, **kwargs):
        region_id = request.POST.get('region')
        region_instance = get_object_or_404(Region, pk=region_id)
        region_instance.is_updated = 'False'
        region_instance.save()
        messages.success(self.request, 'Pomyślnie dodano obszar do aktualizacji')
        return HttpResponseRedirect(reverse('regions:regions'))

    
class AddDriverToRegionView(LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    template_name = "regions/add_driver_to_region.html"
    context_object_name = 'add_driver_region'
    model = Region
    instance = Region.objects.all()[0]
    #success_message = 'Pomyślnie dodano zasoby do regionu'
    #instance = get_object_or_404(Region, pk=self.kwargs['pk']) 
    #zamienić gdy regiony zostaną wprowadzone do bazy danych. Mockup.
    
    def get_queryset(self): 
        return Driver.objects.all()
     
    
    def post(self, request, *args, **kwargs):
        region_id = kwargs['pk']
        driver_id = request.POST.get('driver')
        driver_instance = get_object_or_404(Driver,pk=driver_id)
        region_instance = get_object_or_404(Region,pk=region_id)
        driver_instance.schedule.add(region_instance) #distinct?
        driver_instance.save()
        messages.success(self.request, 'Pomyślnie przypisano zasoby do regionu')
        return HttpResponseRedirect(reverse('regions:regions'))

        #return super().post(request, *args, **kwargs)

		
class EditDriverToRegionView(LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    template_name = "regions/edit_driver_to_region.html"
    context_object_name = 'edit_driver_region'

    def get_queryset(self):
        return Driver.objects.all()

    def post(self, request, *args, **kwargs):
        region_id = kwargs['pk']
        driver_id = request.POST.get('driver')
        driver_instance = get_object_or_404(Driver, pk=driver_id)
        region_instance = get_object_or_404(Region, pk=region_id)
        current_value = driver_instance.full_name
