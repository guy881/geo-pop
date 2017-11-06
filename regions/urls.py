from django.conf.urls import url

from regions.views import regions

urlpatterns = [
    url(r'$', regions, name='regions'),
]
