import datetime
from django.shortcuts import render

from users.models import Lid

from .utils import future_events

from .models import AgendaClient, Event, NIEvent

# Create your views here.
def agenda(request):
    evns = future_events(datetime.datetime.today())
    lid = request.user.lid
    # no_linked_account = False
    # try:
    #     client = AgendaClient.objects.get(lid_id=lid.id)
    # except: 
    #     no_linked_account =True
    #     client = None
    

    content = { 'events':evns}
    return render(request, 'agenda/agenda.html', content)

def dsani(request):
    events = Event.objects.all()
    ni_events = NIEvent.objects.all()
    leden = Lid.objects.all()
    content = {'events': events, 'ni_events': ni_events, 'leden': leden}
    return render(request, 'agenda/dsani.html', content)               