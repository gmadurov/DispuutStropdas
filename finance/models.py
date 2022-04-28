from datetime import datetime
from multiprocessing import Event
import uuid
from django.db import models

from users.models import Lid
from agenda.models import Event

# Create your models here.
def senate_jaar():
    date = datetime.today()
    month = int(date.strftime("%m"))
    year = int(date.strftime("%Y")) -1990
    if month >= 9:
        out = year + 1
    else:
        out = year
    return out
    


class Decla(models.Model):
    # owner, event, content, total, present, senate_year, receipt, reunist, kmters, verwerkt

    owner = models.ForeignKey(Lid, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(max_length=50)
    total = models.FloatField()

    present = models.ManyToManyField(Lid, blank=True, related_name='present_leden')

    senate_year = models.IntegerField(
        default=senate_jaar()
    )
    receipt = models.ImageField(upload_to="declas/")
    reunist = models.IntegerField(default=0)
    kmters = models.IntegerField(default=0)

    verwerkt = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.event) + " " + str(self.owner)

    @property
    def imageURL(self):
        try:
            url = self.lid_image.url
        except:
            url = ""
        return url

    class Meta:
        ordering = ["event"]


class Stand(models.Model):
    owner = models.ForeignKey(Lid, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    def __str__(self):
        return str(self.owner)+', €'+str(self.amount)