from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import CarForm
from .models import Car
from regions.models import Region,GeoLocalization


class CarListView(LoginRequiredMixin, generic.ListView):
    template_name = 'cars/car_list_final.html'
    context_object_name = 'all_cars'

    def get_queryset(self):
        res = Car.objects.all()

        for c in res:
            reg = Region.objects.all().first()
            position = GeoLocalization.objects.get(id=reg.north_west_id)
            c.last_location = position
        return res


class CarCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CarForm
    model = Car
    template_name_suffix = '_add'
    success_url = reverse_lazy('cars:car_list')
    success_message = 'Pomyślnie dodano nowy samochód'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            messages.success(request, 'Pomyślnie anulowano dodawanie samochodu')
            return HttpResponseRedirect(reverse('cars:car_list'))
        else:
            return super(CarCreateView, self).post(request, *args, **kwargs)


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = '__all__'
    template_name_suffix = '_update_form'


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    fields = '__all__'
    template_name_suffix = '_delete_form'
