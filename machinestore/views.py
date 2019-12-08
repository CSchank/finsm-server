from django.shortcuts import render
from django.http import HttpResponse

from .models import Machine

# Create your views here.

def home(request):
    return render(request, "home.html")

def listmachines(request):
    if request.user.is_authenticated and request.method == "POST":
        return HttpResponse("Logged in")
    else:
        return HttpResponse("Unauthorized.", status=401)

def savemachine(request):
    if request.user.is_authenticated and request.method == "POST":
        return HttpResponse()
    else:
        return HttpResponse("Unauthorized.", status=401)

def loadmachine(request):
    print(request.headers)
    if request.user.is_authenticated and request.method == "POST":
        return HttpResponse("Logged in")
    else:
        return HttpResponse("Unauthorized.", status=401)

def archivemachine(request):
    if request.user.is_authenticated and request.method == "POST":
        return HttpResponse("Logged in")
    else:
        return HttpResponse("Unauthorized.", status=401)