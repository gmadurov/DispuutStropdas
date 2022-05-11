from django.shortcuts import render

from finance.models import Stand

from .models import Links

# Create your views here.
def agenda(request):
    link = Links.objects.get(name= 'Agenda')
    content = {'link': link, "stand": Stand.objects.get(owner_id=request.user.lid.id).amount,}
    return render(request, 'links/agenda.html', content)