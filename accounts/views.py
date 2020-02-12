from django.shortcuts import render
from django.http import HttpResponse
import json
from django.apps import apps

MachineStore = apps.get_model('machinestore', 'Machine')

# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginstate(request):
    print(request)
    if request.user.is_authenticated:
        try:
            machine = MachineStore.objects.filter(user=request.user).filter(archived=False).order_by('-edit_date')[0]

            authResponse = {"loggedin": True, "email": request.user.email, "newestMachine": str(machine.uuid) }
        except:
            authResponse = {"loggedin": True, "email": request.user.email, "newestMachine": "" }

        return HttpResponse(json.dumps(authResponse))
    else:
        authResponse = {"loggedin": False}

        return HttpResponse(json.dumps(authResponse))