from django.conf.urls import url

from drivers.views import *

urlpatterns = [
    url(r'list/', DriverList.as_view(), name='list'),
    url(r'schedule/', driver_schedule, name='schedule'),
    url(r'create/', DriverCreateView.as_view(), name='create'),
    url(r'delete/(?P<pk>[0-9]+)/', DriverDeleteView.as_view(), name='delete'),
    url(r'edit/(?P<pk>[0-9]+)/image', DriverEditImage.as_view(), name='edit_image'),
    url(r'edit/(?P<pk>[0-9]+)/basic', DriverEditBasic.as_view(), name='edit_basic'),
    url(r'edit/(?P<pk>[0-9]+)/cars', DriverEditCars.as_view(), name='edit_cars'),
]
