import datetime

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from agenda.models import Event

# def searchLeden(request):
#     search_query = ''
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     lidlist = Lid.objects.distinct().filter(
#         Q(name__icontains=search_query)
#         | Q(short_intro__icontains=search_query))
#     return lidlist, search_query


def future_events(date):
    fut_events = Event.objects.distinct().filter(
        Q(start_date__gte=date) | Q(end_date__gte=date)
    )
    return fut_events


def past_events(date):
    past_events = Event.objects.distinct().filter(
        Q(start_date__lte=date) | Q(end_date__lte=date)
    )
    return past_events


def searchEvents(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    eventlist = Event.objects.distinct().filter(
        Q(summary__icontains=search_query)
        | Q(description__icontains=search_query)
        | Q(start_date__icontains=search_query)
    )
    return eventlist, search_query


def paginateEvents(request, page=1, events=None, results=None, date=None):
    if not events:
        events = Event.objects.all()
    paginator = Paginator(events, results)
    print("Pages", page)
    # paginate the events
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # get the starting page for events
        # if date == None then it gives page = 1 and those events
        # if date!= None returns the current day
        for page in range(1, paginator.num_pages):
            events = paginator.page(page)
            stop = False
            if date:
                for e in events:
                    if e.start_date > date:  # or e.end_date > date:
                        stop = True
                        break
            else:
                break
            if stop:
                break
    except EmptyPage:
        page = paginator.num_pages
        events = paginator.page(page)
    print(paginator.num_pages)
    return events
