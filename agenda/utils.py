
# def searchLeden(request):
#     search_query = ''
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     lidlist = Lid.objects.distinct().filter(
#         Q(name__icontains=search_query)
#         | Q(short_intro__icontains=search_query))
#     return lidlist, search_query


from .models import Event
from django.db.models import Q



def future_events(date):
    fut_events = Event.objects.distinct().filter(
        Q(start_date__gte= date)| Q(end_date__gte=date)
    )
    return fut_events