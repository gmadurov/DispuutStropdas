from django.db.models.signals import post_delete, post_save

# from django.core.mail import send_mail
from django.conf import settings


from .models import Bier, Decla, Stand
from users.models import Lid

EVENT_CHOICES = (
    ("Activiteit", "Activiteit"),
    ("Borrel", "Borrel"),
    ("Clubactiviteit", "Clubactiviteit"),
    ("Wedstrijd", "Wedstrijd"),
    ("Dispuutsactiviteit", "Dispuutsactiviteit"),
    ("Dispuutsverjaardag", "Dispuutsverjaardag"),
    ("Dispuutsavonds", "Dispuutsavonds"),
    ("AdministratifActivitied", "AdministratifActivitied"),
    ("Bier", "Bier"),
)



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
            if decla.verwerkt:
                amount_declared += round(decla.total, 2)
        # print(lid, amount_declared)
        amount_paid = 0
        for decla in declas:
            if decla.verwerkt:
                if not decla.event.summary in ["Borrel","Dispuutsavonds","AdministratifActivitied", "Bier"] :
                    try:
                        amount_pp = round(decla.total / len(decla.present.all()), 2)
                    except:
                        amount_pp = 0
                    for Present in decla.present.all():
                        if lid.id == Present.id:
                            amount_paid += amount_pp
                elif decla.event.summary in ["Bier"]:
                    try:
                       num_biers = int(decla.content)
                       amount_paid += Bier.cost  * num_biers
                    except:pass
                elif decla.event.summary in ["AdministratifActivitied"]:
                    pass

        
        stand.amount = round(stand.initial_amount + amount_declared - amount_paid, 2)
        stand.save()


post_save.connect(updateStand, sender=Decla)
