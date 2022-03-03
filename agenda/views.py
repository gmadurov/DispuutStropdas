import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import EventForm
from users.models import Lid

from .models import AgendaClient, Event, NIEvent
from .utils import future_events


# Create your views here.
@login_required(login_url='fakePage')
def agenda(request):
    evns = future_events((datetime.date.today() - datetime.timedelta(days=1)).isoformat())
    lid = request.user.lid
    # no_linked_account = False
    # try:
    #     client = AgendaClient.objects.get(lid_id=lid.id)
    # except: 
    #     no_linked_account =True
    #     client = None
    

    content = { 'events':evns}
    return render(request, 'agenda/agenda.html', content)

@login_required(login_url='fakePage')
def dsani(request):
    events = Event.objects.all()
    ni_events = NIEvent.objects.all()
    leden = Lid.objects.all()
    content = {'events': events, 'ni_events': ni_events, 'leden': leden}
    return render(request, 'agenda/dsani.html', content)               


@login_required(login_url='login')
def create_event(request):
    form = EventForm()
    if request.method == 'POST':  # checks the method
        # creates the form object
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():  # if its valid
            form.save()  # save the object to database
            messages.info(request, 'Event was created')
            return redirect('agenda')
    context = {'form': form}
    return render(request, "agenda/event-form.html", context)


def edit_event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == 'POST':  # checks the method
        # creates the form object
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():  # if its valid
            form.save()  # save the object to database
            messages.info(request, 'Event was edited')
            return redirect('agenda')
    context = {'form': form}
    return render(request, "agenda/event-form.html", context)
from django import template

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 