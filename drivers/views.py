from django.shortcuts import render
from .models import Driver


# Create your views here.
def drivers(request):

    all_drivers = Driver.objects.all()

    template_data = {
        'driver_list': all_drivers
    }
    return render(request, "drivers/list.html", template_data)
