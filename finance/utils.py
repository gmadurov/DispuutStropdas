from .models import Stand, Decla
from users.models import Lid


def recalculate_all_Stands():
    declas = Decla.objects.all()
    leden = Lid.objects.all()


    # for each lid fist calculate how much the have declared and then how much has been paid for them 
    for lid in leden:
        declaS = Decla.objects.filter(owner_id = lid.id)
        stand = Stand.objects.get(owner_id = lid.id)
        amount_declared = 0 
        for decla in declaS:
            amount_declared += decla.total
        # print(lid, amount_declared)
        amount_paid = 0 
        for decla in declas:
            try:amount_pp = round(decla.total/len(decla.present.all()),2)
            except: amount_pp = 0
            for Present in decla.present.all():
                if lid.id == Present.id:
                    amount_paid += amount_pp


        stand.amount = amount_declared - amount_paid
        stand.save()
        # print(lid, amount_paid)
        