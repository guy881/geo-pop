from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Driver


def drivers(request):

    all_drivers = Driver.objects.all()

    template_data = {
        'driver_list': all_drivers
    }
    return render(request, "drivers/list.html", template_data)


def add(request):

    if request.method == 'POST':
        # TODO: create driver from form data
        return HttpResponseRedirect('/drivers')
    else:
        return render(request, "drivers/add.html")
