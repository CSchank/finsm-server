from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginstate(request):
    print(request)
    if request.user.is_authenticated:
        authResponse = {"loggedin": True, "email": request.user.email}

        return HttpResponse(json.dumps(authResponse))
    else:
        authResponse = {"loggedin": False, "email": ""}

        return HttpResponse(json.dumps(authResponse))