import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from finance.models import Stand
from users.models import Lid

from .forms import EventForm, NIEventForm
from .models import Event, NIEvent
from .signals import get_service
from .utils import future_events, past_events, searchEvents, paginateEvents

# Create your views here.
@login_required(login_url="fakePage")
def agenda(request):
    FUevns = future_events(
        (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    )
    FUevns, search_query = searchEvents(request)
    custom_range, FUevns = paginateEvents(request, FUevns, 20, datetime.date.today())
    lid = request.user.lid
    try:
        pass
        # refresh the token of the agenda
        # (get_service(True))
    except:
        messages.error(request, "token not updated")
        pass

    content = {
        "events": FUevns,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "agenda/agenda.html", content)


@login_required(login_url="fakePage")
def afgelopenAgenda(request):
    evns = past_events((datetime.date.today() - datetime.timedelta(days=1)).isoformat())
    evns, search_query = searchEvents(request)
    custom_range, evns = paginateEvents(request, evns, 25)
    lid = request.user.lid

    content = {
        "events": evns,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "agenda/afgelopen-agenda.html", content)


@login_required(login_url="fakePage")
def dsani(request):
    # ni_events = NIEvent.objects.all()
    events = future_events(
        (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    )
    events, search_query = searchEvents(request)
    custom_range, events = paginateEvents(request, events, 10, datetime.date.today())

    leden = NIEvent.objects.filter(lid=request.user.lid)
    # dic_NI = {}
    # for ev in events:
    #     dic_NI[ev] = NIEvent.objects.filter(lid=request.user.lid, event=ev)
    leden = Lid.objects.filter(active=True)
    # print(events)
    content = {
        "events": events,
        "leden": leden,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "agenda/dsani.html", content)


@login_required(login_url="login")
def create_event(request):
    form = EventForm()
    if request.method == "POST":  # checks the method
        # creates the form object
        form = EventForm(request.POST)
        if form.is_valid():  # if its valid
            event = form.save(commit=False)  # save the object to database
            if not event.end_date:
                event.end_date = event.start_date
            if not event.end_time and event.start_time:
                event.end_time = event.start_time
            elif not event.end_time:
                event.end_time = datetime.datetime.min.time()
            if not event.start_time:
                event.start_time = datetime.datetime.min.time()
            if event.end_date < event.start_date:
                event.end_date, event.start_date = event.start_date, event.end_date
            event.save()
            messages.info(request, "Event was created")
            return redirect("agenda")
    context = {
        "form": form,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "agenda/event-form.html", context)


@login_required(login_url="login")
def edit_event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == "POST":  # checks the method
        # creates the form object
        form = EventForm(request.POST, instance=event)
        if form.is_valid():  # if its valid
            event = form.save(commit=False)  # save the object to database
            if not event.end_date:
                event.end_date = event.start_date
            if not event.end_time and event.start_time:
                event.end_time = event.start_time
            elif not event.end_time:
                event.end_time = datetime.datetime.min.time()
            if not event.start_time:
                event.start_time = datetime.datetime.min.time()
            if event.end_date < event.start_date:
                event.end_date, event.start_date = event.start_date, event.end_date
            event.save()
            messages.info(request, "Event was edited")
            return redirect("agenda")
    context = {
        "form": form,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "agenda/event-form.html", context)


@login_required(login_url="login")
def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        messages.info(request, "Event deleted")
        return redirect("agenda")
    content = {
        "object": event,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "delete-template.html", content)


@login_required(login_url="login")
def edit_dsani(request, pk):
    lid = request.user.lid
    nievent = NIEvent.objects.get(id=pk)
    form = NIEventForm(instance=nievent)
    if request.method == "POST":  # checks the method
        # creates the form object
        form = NIEventForm(request.POST, instance=nievent)
        if form.is_valid():  # if its valid
            form.save()  # save the object to database
            messages.info(request, "Neuk Index was edited")
            return redirect("DSANI")
    context = {
        "form": form,
        "event": nievent,
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "agenda/Neuk_index_form.html", context)


@login_required(login_url="login")
def try_out(request):
    context = {
        "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,
    }
    return render(request, "try_out.html", context)
