from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView


class FinsmAppView(TemplateView):
    template_name = "index.html"

class FinsmJSView(TemplateView):
    template_name = "finsm.min.js"