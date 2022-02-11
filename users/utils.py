from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Lid
from django.db.models import Q


def searchLeden(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    lidlist = Lid.objects.distinct().filter(
        Q(name__icontains=search_query)
        | Q(short_intro__icontains=search_query))
    return lidlist, search_query


def paginateLeden(request, leden, results):
    page = request.GET.get('page')
    paginator = Paginator(leden, results)

    try:
        leden = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        leden = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        leden = paginator.page(page)
    span = 4
    leftIndex = (int(page) - span)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+span+1)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    custom_range = range(leftIndex, rightIndex)

    return custom_range, leden
