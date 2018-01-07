from django.conf.urls import url

from updates.views import *

urlpatterns = [
    url(r'list/', UpdatesHistoryListView.as_view(), name='updates_history_list'),
]
