from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logut
from django.shortcuts import render


# Create your views here.
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
                    return HttpResponseRedirect("/admin")
            else:
                error = 'Niepoprawne dane użytkownika'
    return render(request, "users/login.html", {"error": error})


def logout(request):
    auth_logut(request)
    return HttpResponseRedirect('/login')
