from django.contrib import admin
from .models import LaTeXExpr

class LaTeXAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date',)

# Register your models here.

admin.site.register(LaTeXExpr, LaTeXAdmin)