from django.shortcuts import render
from django.http import HttpResponse
from .models import LaTeXExpr
import requests
import json

# Create your views here.
def renderlatex(request, expr):
    query = LaTeXExpr.objects.filter(expression=expr)
    if query.exists():
        latexExpr = query.first()
        svg_data = latexExpr.svg_data
        latexExpr.accesses += 1
        latexExpr.save()
        return HttpResponse(svg_data,content_type="image/svg+xml")
    else:
        data = {
                "format": "TeX",
                "math": expr,
                "svg": True,
                "mml": False,
                "png": False,
                "speakText": True,
                "speakRuleset": "mathspeak",
                "speakStyle": "default",
                "ex": 6,
                "width": 100,
                "linebreaks": False,
            }
        jsondata = json.dumps(data)
        r = requests.post(url="http://localhost:8003",data=jsondata)
        print(r.status_code)
        svg_data=r.text
        if r.status_code == 200:
            new_expr = LaTeXExpr(expression=expr, svg_data=svg_data)
            new_expr.save()
        return HttpResponse(svg_data,content_type="image/svg+xml")
