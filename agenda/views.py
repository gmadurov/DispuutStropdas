import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import EventForm, NIEventForm
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
    lid_NI = NIEvent.objects.filter(lid=request.user.lid)
    dic_NI = {}
    for ev in events:
        dic_NI[ev] = (NIEvent.objects.filter(lid=request.user.lid, event = ev))
        # print(ev)
        # print(dic_NI[ev])
    leden = Lid.objects.all()
    content = {'events': events, 'ni_events': ni_events, 'leden': leden, 'dic_NI':dic_NI}
    return render(request, 'agenda/dsani.html', content)               


@login_required(login_url='login')
def create_event(request):
    form = EventForm()
    if request.method == 'POST':  # checks the method
        # creates the form object
        form = EventForm(request.POST)
        if form.is_valid():  # if its valid
            form.save()  # save the object to database
            messages.info(request, 'Event was created')
            return redirect('agenda')
    context = {'form': form}
    return render(request, "agenda/event-form.html", context)


@login_required(login_url='login')
def edit_event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == 'POST':  # checks the method
        # creates the form object
        form = EventForm(request.POST, instance= event)
        if form.is_valid():  # if its valid
            form.save()  # save the object to database
            messages.info(request, 'Event was edited')
            return redirect('agenda')
    context = {'form': form}
    return render(request, "agenda/event-form.html", context)

@login_required(login_url='login')
def edit_dsani(request,  pk):
    lid = request.user.lid
    nievent = NIEvent.objects.get(id=pk)
    form = NIEventForm(instance=nievent)
    if request.method == 'POST':  # checks the method
        # creates the form object
        form = NIEventForm(request.POST, instance=nievent)
        if form.is_valid():  # if its valid
            form.save()  # save the object to database
            messages.info(request, 'Neuk Index was edited')
            return redirect('DSANI')
    context = {'form': form, 'event': nievent}
    return render(request, "agenda/Neuk_index_form.html", context)
