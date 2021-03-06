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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from cars.views import *
from drivers.views import *
from regions.views import *
from updates.views import CreateUpdateAPI
from users.views import *
from updates.views import *


# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'driver-api', DriverDetailAPIView.as_view(), 'Driver')
# print(router.urls)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-driver/', DriverDetailAPIView.as_view()),
    url(r'^create-update/', CreateUpdateAPI.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^drivers/', include('drivers.urls', namespace='drivers'), ),
    url(r'^cars/', include('cars.urls', namespace='cars'), ),
    url(r'^updates/', include('updates.urls', namespace='updates'), ),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^', include('regions.urls', namespace='regions'), ),
]
