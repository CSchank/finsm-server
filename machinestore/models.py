from django.db import models

import uuid
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Machine(models.Model):

    class MachineType(models.TextChoices):
        DFA = 'D', _("DFA")
        NFA = 'N', _("NFA")
        NPDA = 'P', _("NPDA")
        TURING = 'T', _("Turing")

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    machine_json = JSONField(default=dict)
    tape_json = JSONField(default=dict)
    archived = models.BooleanField(default=False)
    machine_type = models.CharField(
        max_length=1,
        choices=MachineType.choices,
        default=MachineType.DFA,
    )
