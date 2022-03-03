from django.db import models

from users.models import Lid

# Create your models here.


class AgendaClient(models.Model):
    lid = models.ForeignKey(Lid, on_delete=models.CASCADE)
    token = models.CharField(max_length=200, null=True, blank=True)
    refresh_token = models.CharField(max_length=200, null=True, blank=True)
    token_uri = models.CharField(max_length=200, null=True, blank=True)
    client_id = models.CharField(max_length=200, null=True, blank=True)
    client_secret = models.CharField(max_length=200, null=True, blank=True)
    scopes = models.CharField(max_length=2000, null=True, blank=True)
    expiry = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
      return str(self.lid.name)


class Event(models.Model):
    
    summary = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField()
    end_time = models.TimeField(null=True, blank=True)
    recuring = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    kokers = models.CharField(max_length=50, null=True, blank=True)
    kartrekkers = models.CharField(max_length=50, null=True, blank=True)
    budget = models.CharField(max_length=50, null=True, blank=True)
    bijzonderheden = models.CharField(max_length=50, null=True, blank=True)
    # Datum	Activiteit	Kokers	Omschrijving	Kartrekkers	Bijzonderheden	Budget
    def __str__(self):
        return str(self.summary)+ ','+ str(self.start_date)
    class Meta:
        ordering = ['start_date', 'start_time','-end_date']

class NIEvent(models.Model):
    '''DSANI events links'''
    event = models.ForeignKey(Event, on_delete= models.CASCADE, related_name='dsani_ev')
    lid = models.ForeignKey(Lid, on_delete= models.CASCADE)
    points = models.IntegerField()
    note = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        if self.note:
            return str(self.lid.initials)+ ', '+ str(self.note)
        return str(self.lid.initials)+ ', '+ str(self.event.description)
        