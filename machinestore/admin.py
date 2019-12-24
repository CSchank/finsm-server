from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Machine

class MachinestoreAdmin(admin.ModelAdmin):
    list_display = ('id','user','name','create_date','edit_date','archived')

    readonly_fields = ('create_date',)

# Register your models here.

admin.site.register(Machine, MachinestoreAdmin)