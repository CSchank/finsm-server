from django.shortcuts import render
from django.http import HttpResponse
from machinestore.models import *

from .models import Machine
import json


# Create your views here.

def home(request):
    return render(request, "home.html")

def listmachines(request):
    if request.user.is_authenticated and request.method == "POST":
        machines = Machine.objects.get(user=request.user)

        machineDicts = []
        for m in machines:
            machineDicts.append({ "id" : m.id, "name" : m.name, "date": m.date.edit_date.timestamp(), "desc": m.desc })

        machinesJson = json.dumps(machineDicts)

        return HttpResponse(machinesJson)

    else:
        return HttpResponse("Unauthorized.", status=401)

def savemachine(request):
    if request.user.is_authenticated and request.method == "POST":
        data = json.loads(request.body)

        name = data["name"]
        desc = data["desc"]
        machine = data["machine"]
        version = data["v"]
        uuid = data["uuid"]
        input_tape = data["tape"]

        newuuid = ""

        if uuid == "":
            new_machine = Machine(name=name, description=desc, user = request.user, tape_json = input_tape, machine_json=machine)
            newuuid = str(new_machine.id)
            new_machine.save()
        else:
            try:
                existing_machine = Machine.objects.get(id=uuid)
                # ensure that the user owns the machine they're trying to edit
                if existing_machine.user == request.user:
                    newuuid = str(existing_machine.id)
                    existing_machine.name = name
                    existing_machine.desc = desc
                    existing_machine.version = version
                    existing_machine.tape_json = input_tape
                    existing_machine.machine_json = machine
                    existing_machine.save()
                else:
                    saveResponse = { "success": False, "uuid": "" }
                    return HttpResponse(json.dumps(saveResponse), status=401)
            except (Machine.DoesNotExist):  # machine does not exist for some reason, so create a new one
                new_machine = Machine(name=name, description=desc, machine_json=machine, user=request.user, tape_json = input_tape)
                newuuid = str(new_machine.id)
                new_machine.save()

        saveResponse = { "success": True, "uuid": newuuid }
        return HttpResponse(json.dumps(saveResponse))
    else:
        saveResponse = { "success": False, "uuid": "" }
        return HttpResponse(json.dumps(saveResponse), status=401)

def loadmachine(request):
    uuid = request.body

    # ensure the user is logged in and the method is POST
    if request.user.is_authenticated and request.method == "POST":
        try:
            existing_machine = Machine.objects.get(id=uuid)
            # ensure that the user owns the machine they're trying to edit
            if existing_machine.user == request.user:
                response_json = { "machine": existing_machine.machine_json, "tape": existing_machine.tape_json}
                return HttpResponse(json.dumps(response_json))
            else:
                fail_response = { "success": False, "uuid": "" }
                return HttpResponse(json.dumps(fail_response), status=401)
        except(Machine.DoesNotExist):
            fail_response = { "success": False, "uuid": "" }
            return HttpResponse(json.dumps(fail_response), status=401)
    else:
        return HttpResponse("Unauthorized.", status=401)

def archivemachine(request):
    if request.user.is_authenticated and request.method == "POST":
        return HttpResponse("Logged in")
    else:
        return HttpResponse("Unauthorized.", status=401)