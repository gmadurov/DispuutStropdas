import datetime
from django.shortcuts import render

from .utils import future_events

from .models import AgendaClient, Event

# Create your views here.
def agenda(request):
    evns = future_events(datetime.datetime.today())
    lid = request.user.lid
    no_linked_account = False
    try:
        client = AgendaClient.objects.get(lid_id=lid.id)
    except: 
        no_linked_account =True
        client = None
    

    content = {'no_linked_account': no_linked_account, 'client': client, 'events':evns}
    return render(request, 'agenda/agenda.html', content)
