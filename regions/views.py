from django.template import  RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Region
from drivers.models import Driver
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import ast


class RegionsView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = "regions/regions.html"

    def get(self, request):
        regions = Region.objects.all()
        #GeoLocalization.objects.all().delete()
        #Region.objects.all().delete()
        regions = Region.objects.all()

        nlat=[]
        nlon=[]
        slat = []
        slon = []
        rupdate=[]
        for i in range (0, regions.count()) :
            nlat.append(float(regions.select_related('north_west__latitude').values_list('north_west__latitude')[i][0]))
            nlon.append(float(regions.select_related('north_west__longitude').values_list('north_west__longitude')[i][0]))
            slat.append(float(regions.select_related('south_east__latitude').values_list('south_east__latitude')[i][0]))
            slon.append(float(regions.select_related('south_east__longitude').values_list('south_east__longitude')[i][0]))
            rupdate.append(int(regions.select_related('is_updated').values_list('is_updated')[i][0]))
        return render(request, 'regions/regions.html', {"nlat": nlat, "nlon": nlon, "slat":slat, "slon":slon, "rupdate":rupdate})

    
    
class AddDriverToRegionView(LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    template_name = "regions/add_driver_to_region.html"
    context_object_name = 'add_driver_region'
    model = Region
    instance = Region.objects.all()[0]
    success_message = 'Pomyślnie dodano zasoby do regionu'
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
        #kwargs['success'] = _('Data saved correctly!')
        messages.success(self.request, 'Pomyślnie przypisano zasoby do regionu')
        return HttpResponseRedirect(reverse('regions:regions'))

        #return super().post(request, *args, **kwargs)


		
        
#def manualActualization(request):
#	return HttpResponse("Ręczna aktualizacja stanu dróg")
#	
#
#def actualUpdates(request):
#	return HttpResponse("Wyświetl aktualnie przeprowadzane aktualizacje")
#	
#	
#def updatesHistory(request):
#	return HttpResponse("Historia aktualizacji")