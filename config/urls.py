"""geopop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL
     to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from users.views import *
from drivers.views import *
from cars.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^driver_list/', DriverList.as_view(), name='driver_list'),
    url(r'^driver_create/', DriverCreateView.as_view(), name='driver_create'),
    url(r'edit/(?P<pk>[0-9]+)/image', DriverEditImage.as_view(), name='driver_image'),
    url(r'edit/(?P<pk>[0-9]+)/basic', DriverEditBasic.as_view(), name='driver_edit_basic'),

    url(r'edit/(?P<pk>[0-9]+)/cars', DriverEditCars.as_view(), name='driver_edit_cars'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^car_list/', CarListView.as_view(), name='car_list'),
    url(r'^car_create/', CarCreateView.as_view(), name='car_create'),
]
