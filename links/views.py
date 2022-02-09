from django.shortcuts import render

from .models import Links

# Create your views here.
def agenda(request):
    link = Links.objects.get(name= 'Agenda')
    content = {'link': link}
    return render(request, 'links/agenda.html', content)