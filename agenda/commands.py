


from agenda.models import NIEvent
def deleteDSANI():
    return NIEvent.objects.all().delete()

