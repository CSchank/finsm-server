from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginstate(request):
    if request.user.is_authenticated:
        return HttpResponse("Logged in")
    else:
        return HttpResponse("Not logged in")