from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Machine(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)
    edit_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    machine_json = models.TextField()
