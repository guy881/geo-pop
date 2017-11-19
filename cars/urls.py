from django.conf.urls import url

from cars.views import *

urlpatterns = [
    url(r'list/', CarListView.as_view(), name='car_list'),
    url(r'create/', CarCreateView.as_view(), name='car_create'),
]
