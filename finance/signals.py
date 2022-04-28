
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

# from django.core.mail import send_mail
from django.conf import settings


from .models import Decla, Stand


def updateStand(sender, instance, created, **kwargs):
    # TODO: find a way to differentiate between senaat years 
    decla = instance
    amount_pp = round(decla.total/len(decla.present.all()),2)
    # add money to the person declaring the decla
    stand = Stand.objects.get(owner_id = decla.owner.id)
    stand.amount += decla.total
    stand.save()
    # take a way a share of the total price for every person present
    for lid in decla.present.all():
        stand = Stand.objects.get(owner_id = lid.id)
        stand.amount -= amount_pp
        stand.save()
        # print(stand, amount_pp)








    # # for decla in declas:
    # amount_pp = int(decla.total/len(decla.present.all()))
    # for lid in decla.present.all():
        
    #     LID = Lid.objects.get(id = lid.id)
    #     print(LID,LID.stand)
    #     LID.stand=LID.stand- amount_pp
    #     print(LID,LID.stand)
    #     LID.save()
    
    
    # def stand_update(self):
        # declas that have been paid for lid
    # declas = Decla.objects.filter(present = self.owner)
    # for decla in declas:
    # amount_pp = int(decla.total/len(decla.present.all()))
    # self.stand -= amount_pp

    # # declared decla where lid paid 
    # declas = Decla.objects.filter(owner = self.owner)
    # for decla in declas:
    #     self.stand += int(decla.total)
post_save.connect(updateStand, sender = Decla)
