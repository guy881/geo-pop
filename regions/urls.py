from django.conf.urls import url
from regions.views import RegionsView, AddDriverToRegionView


urlpatterns = [
    url(r'$', RegionsView.as_view(), name='regions'),
    url(r'regions/add/', AddDriverToRegionView.as_view(), name='addDriverToRegionView'),
]
