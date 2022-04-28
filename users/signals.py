# these 2 things are the same
# post_save.connect(lidUpdated, sender=Lid)
# @receiver(post_save, sender= Lid)


from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from finance.models import Stand


from .models import Lid


def createStand(sender, instance, created, **kwargs):
    if created:
        user = instance
        stand = Stand.objects.create(owner=user.lid)


def createLid(sender, instance, created, **kwargs):
    if created:
        user = instance
        lid = Lid.objects.create(
            user=user, email=user.email, name=user.first_name + user.last_name
        )
    else:
        user = instance
        lid = user.lid
        lid.name = user.first_name + user.last_name
        if user.email:
            lid.email = user.email
        subject = " welcome to "
        message = " thanks for joining"
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [lid.email],
        #     fail_silently = False
        # )


# @receiver(post_delete, sender= Lid)


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


def updateUser(sender, instance, created, **kwargs):
    lid = instance
    user = lid.user
    if not created:
        try:
            user.first_name, user.last_name = lid.name.split(" ")
        except:
            user.first_name = lid.name
        user.email = lid.email
        user.save()
        return


post_save.connect(createStand, sender=User)
post_save.connect(createLid, sender=User)
post_save.connect(updateUser, sender=Lid)
post_delete.connect(deleteUser, sender=Lid)
