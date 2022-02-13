from django.contrib import admin

from agenda.models import AgendaClient, Event, NIEvent

# Register your models here.
admin.site.register(AgendaClient)
admin.site.register(Event)
admin.site.register(NIEvent)