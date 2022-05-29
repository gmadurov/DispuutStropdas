

from agenda.models import NIEvent

def deleteDSANI():
    return NIEvent.objects.all().delete()

from agenda.models import Event
def delEvents():
    return Event.objects.all().delete()