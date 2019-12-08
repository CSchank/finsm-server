from django.urls import path

from . import views

urlpatterns = [
    path('machine/list', views.listmachines, name='list_machines'),
    path('machine/save', views.savemachine, name='list_machines'),
    path('machine/load', views.loadmachine, name='list_machines'),
    path('machine/archive', views.archivemachine, name='list_machines'),
]