from django.db import models

import uuid
from django.contrib.auth.models import User

# Create your models here.

class Machine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    create_date = models.DateField(auto_now_add=True)
    edit_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    machine_json = models.TextField(default="")
    tape_json = models.TextField(default="")
