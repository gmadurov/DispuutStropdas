from datetime import datetime
import uuid
from django.db import models

from users.models import Lid

def senate_jaar():
    date = datetime.today()
    month = int(date.strftime("%m"))
    year = int(date.strftime("%Y")) -1990
    if month >= 9:
        out = year + 1
    else:
        out = year
    return out
# Create your models here.
class Document(models.Model):

    owner = models.ForeignKey(Lid, on_delete=models.CASCADE,  null=True, blank=True)
    name = models.CharField(max_length=30)
    senate_year = models.IntegerField(default = senate_jaar())
    file = models.FileField(
        upload_to='documents/', null=True, blank=True)
    show = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return (self.name+' '+ str(self.senate_year))
    class Meta:
        ordering = ['senate_year']