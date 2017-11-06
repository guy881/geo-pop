from django.conf.urls import url
from regions.views import RegionsView


urlpatterns = [
    url(r'$', RegionsView.as_view(), name='regions'),
]
