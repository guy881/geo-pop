from django.conf.urls import url
from regions.views import RegionsView, AddDriverToRegionView


urlpatterns = [
    url(r'^regions/add/(?P<pk>[0-9]+)', AddDriverToRegionView.as_view(), name='addDriverToRegionView'),
    url(r'$', RegionsView.as_view(), name='regions'),
]
