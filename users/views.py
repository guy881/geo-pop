from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logut
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets

from users.models import CustomUser
from users.serializers import CustomUserSerializer


def login(request):
    error = ''
    if request.method == "POST":
        if request.POST.get('non_field_errors', False):
            error = request.POST['non_field_errors']
        elif request.POST.get('username', False):
            username = request.POST.get('username')
            password = request.POST.get('pwd')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect("/")
            else:
                error = 'Niepoprawne dane użytkownika'
    return render(request, "users/login.html", {"error": error})


def logout(request):
    auth_logut(request)
    return HttpResponseRedirect('/login')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
