from django.db.models.signals import post_delete, post_save

# from django.core.mail import send_mail
from django.conf import settings


from .models import Decla, Stand
from users.models import Lid


def updateStand(sender, instance, **kwargs):
    """recalculates the stand of each member every time a new decla has been filled in"""
    # TODO: find a way to differentiate between senaat years
    declas = Decla.objects.all()
    leden = Lid.objects.all()
    # for each lid fist calculate how much the have declared and then how much has been paid for them
    for lid in leden:
        declaS = Decla.objects.filter(owner_id=lid.id)
        stand = Stand.objects.get(owner_id=lid.id)
        amount_declared = 0
        for decla in declaS:
            amount_declared += decla.total
        # print(lid, amount_declared)
        amount_paid = 0
        for decla in declas:
            if not decla.event.summary == "Borrel":
                try:
                    amount_pp = round(decla.total / len(decla.present.all()), 2)
                except:
                    amount_pp = 0
                for Present in decla.present.all():
                    if lid.id == Present.id:
                        amount_paid += amount_pp
        stand.amount = amount_declared - amount_paid
        stand.save()


post_save.connect(updateStand, sender=Decla)
