from django.shortcuts import render
from django.http import HttpResponse
from machinestore.models import *

from .models import Machine
import json
import time


# Create your views here.

def home(request):
    return render(request, "home.html")

def listmachines(request):
    if request.user.is_authenticated and request.method == "POST":
        machine_filter = request.body.decode('utf-8')

        if machine_filter == "all":
            machines = Machine.objects.filter(user=request.user, archived=False).order_by("-edit_date")
        elif machine_filter == "arc":
            machines = Machine.objects.filter(user=request.user, archived=True).order_by("-edit_date")
        else:
            machines = Machine.objects.filter(user=request.user, archived=False, machine_type=machine_filter).order_by("-edit_date")

        time.sleep(20)

        machineDicts = [{ "v":      1
                        , "id":     str(m.uuid)
                        , "name":   m.name
                        , "date":   int(m.edit_date.timestamp() * 1000)
                        , "desc":   m.description
                        , "type":   m.machine_type
                        } for m in machines
                        ]
        return HttpResponse(json.dumps(machineDicts))
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
            newuuid = str(new_machine.uuid)
            new_machine.save()
        else:
            try:
                existing_machine = Machine.objects.get(uuid=uuid)
                # ensure that the user owns the machine they're trying to edit
                if existing_machine.user == request.user:
                    newuuid = str(existing_machine.uuid)
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
                newuuid = str(new_machine.uuid)
                new_machine.save()

        saveResponse = { "success": True, "uuid": newuuid }
        return HttpResponse(json.dumps(saveResponse))
    else:
        saveResponse = { "success": False, "uuid": "" }
        return HttpResponse(json.dumps(saveResponse), status=401)

def loadmachine(request):
    uuid = json.loads(request.body)

    # ensure the user is logged in and the method is POST
    if request.user.is_authenticated and request.method == "POST":
        try:
            existing_machine = Machine.objects.get(uuid=uuid)
            # ensure that the user owns the machine they're trying to edit
            if existing_machine.user == request.user:
                response_json = { "machine": existing_machine.machine_json, "tape": existing_machine.tape_json, "name": existing_machine.name, "uuid": uuid }
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
    data = json.loads(request.body)

    uuid = data["uuid"]
    restore = data["restore"]

    if request.user.is_authenticated and request.method == "POST":
        try:
            existing_machine = Machine.objects.get(uuid=uuid)
            # ensure that the user owns the machine they're trying to edit
            if existing_machine.user == request.user:
                existing_machine.archived = not restore

                existing_machine.save()

                archiveResponse = { "success": True }
                return HttpResponse(json.dumps(archiveResponse))
            else:
                archiveResponse = { "success": False }
                return HttpResponse(json.dumps(archiveResponse), status=401)
        except (Machine.DoesNotExist):  # machine does not exist for some reason, so create a new one
            new_machine = Machine(name=name, description=desc, machine_json=machine, user=request.user, tape_json = input_tape)
            newuuid = str(new_machine.uuid)
            new_machine.save()
    else:
        return HttpResponse("Unauthorized.", status=401)