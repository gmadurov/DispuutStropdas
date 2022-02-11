from django.contrib import admin

from agenda.models import AgendaClient, Event

# Register your models here.
admin.site.register(AgendaClient)
admin.site.register(Event)
