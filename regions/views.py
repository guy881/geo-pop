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
        context['updated_percentage'] = get_update_percentage()
        context['outdated_percentage'] = 100 - get_update_percentage()
        return context

    def post(self, request, *args, **kwargs):
        region_id = request.POST.get('region')
        functionInfo = request.POST.get('message')
        region_instance = get_object_or_404(Region, pk=region_id)
        if (functionInfo == "markToActualize"):
            region_instance.is_updated = 'False'
            region_instance.save()
        elif (functionInfo == "markAsUpdated"):
            if not region_instance.is_updated:
                region_instance.is_updated = 'True'
                region_instance.save()
        messages.success(self.request, 'Pomyślnie dodano obszar do aktualizacji')
        return HttpResponseRedirect(reverse('regions:regions'))


class AddDriverToRegionView(LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    template_name = "regions/add_driver_to_region.html"
    context_object_name = 'add_driver_region'
    model = Region
    #instance = Region.objects.all()[0]
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

        driver_instance.schedule.clear()
        driver_instance.schedule.add(region_instance) #distinct?
        driver_instance.save()
        messages.success(self.request, 'Pomyślnie przypisano zasoby do regionu')

        #for driver in region_instance.driver_set.all():
        #    print(driver.full_name)



        return HttpResponseRedirect(reverse('regions:regions'))

        #return super().post(request, *args, **kwargs)


class editDriverToRegionDto(object):
    allDrivers = [],
    selectedDriver = 0

    def __init__(self, allDrivers, selectedDriver):
        self.allDrivers = allDrivers
        self.selectedDriver = selectedDriver


class EditDriverToRegionView(LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    template_name = "regions/edit_driver_to_region.html"
    context_object_name = 'edit_driver_region'

    def get_queryset(self):
        region_id = self.kwargs['pk']
        region_instance = get_object_or_404(Region, pk=region_id)

        lastIndex = region_instance.driver_set.all().count()-1
        if(lastIndex<0):
            current_value = 0
        else:
            driver_instance = region_instance.driver_set.all()[lastIndex]
            current_value = driver_instance.id

        dto = editDriverToRegionDto(Driver.objects.all(), current_value)
        return dto

    def post(self, request, *args, **kwargs):
        region_id = kwargs['pk']
        driver_id = request.POST.get('driver')
        driver_instance = get_object_or_404(Driver, pk=driver_id)
        region_instance = get_object_or_404(Region, pk=region_id)

        driver_instance.schedule.clear()
        driver_instance.schedule.add(region_instance)  # distinct?

        driver_instance.save()
        messages.success(self.request, 'Zapisano')

        # for driver in region_instance.driver_set.all():
        #    print(driver.full_name)



        return HttpResponseRedirect(reverse('regions:regions'))

def get_update_percentage():
    return int(float(truncate(float(len(Region.objects.filter(is_updated=True))/len(Region.objects.all())),2))*100)

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])
