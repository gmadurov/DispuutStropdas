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
    '''event = {
      'summary': 'Google I/O 2015',
      'location': '800 Howard St., San Francisco, CA 94103',
      'description': 'A chance to hear more about Google\'s developer products.',
      'start': {
        'dateTime': '2015-05-28T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': '2015-05-28T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=2'
      ],
      'attendees': [
        {'email': 'lpage@example.com'},
        {'email': 'sbrin@example.com'},
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }
    '''
    # owner = models.ForeignKey(Lid)
    summary = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    recuring = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    kokers = models.CharField(max_length=50, null=True, blank=True)
    kartrekkers = models.CharField(max_length=50, null=True, blank=True)
    budget = models.CharField(max_length=50, null=True, blank=True)
    bijzonderheden = models.CharField(max_length=50, null=True, blank=True)
    # Datum	Activiteit	Kokers	Omschrijving	Kartrekkers	Bijzonderheden	Budget
    def __str__(self):
      return str(self.summary)+ ','+ str(self.start_time)