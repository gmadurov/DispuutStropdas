from __future__ import print_function

import datetime
import os.path
from pathlib import Path
from django.contrib import messages


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from users.models import Lid

from .models import Event, NIEvent


from django.db.models.signals import post_delete, post_save



# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events','https://www.googleapis.com/auth/calendar.events.readonly','https://www.googleapis.com/auth/calendar.readonly']

def events_add(sender, instance=None,  **kwargs):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(Path(__file__).resolve().parent/'token.json'):
        creds = Credentials.from_authorized_user_file(Path(__file__).resolve().parent/'token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                Path(__file__).resolve().parent/'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(Path(__file__).resolve().parent/'token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        for evs in Event.objects.all():
            event ={
            'summary': evs.summary,
            'location': evs.location or "",
            'description': evs.description or "",
            'start': {
                'dateTime': evs.start_time.isoformat(),
                'timeZone': 'Europe/Amsterdam',
            },
            'end': {
                'dateTime': evs.end_time.isoformat() ,
                'timeZone': 'Europe/Amsterdam',
            },
            'recurrence': [
            ],
            
            'reminders': {
            }
            }
        event = service.events().insert(calendarId='primary', body=event).execute()

    except HttpError as error:
        # print('An error occurred: %s' % error)
        pass

def create_NI_event(sender, instance,created,  **kwargs):
    '''creates NI events when a new event is created '''
    if created:
        leden = Lid.objects.all()
        even = instance
        for li in leden: 
            ni = NIEvent.objects.create(
                event = even,
                points = 0,
                lid = li,
                note = '',
            )
def create_NI_user(sender, instance,created,  **kwargs):
    '''creates NI events when a new profile is created '''
    if created:
        Events = Event.objects.all()
        lid = instance.user.lid
        for ev in Events: 
            ni = NIEvent.objects.create(
                event = ev,
                points = 0,
                lid = lid,
                note = '',
            )
# def Update_DSANI_Events(sender,instance,created,**kwargs):
#     if created:
#         for LID in Lid.objects.all():
#                 ni = NIEvent.objects.create(
#                     event = instance,
#                     points = 0,
#                     lid = LID,
#                     note = '',
#                 )
                # print(EVENT, LID)

post_save.connect(create_NI_event, sender=Event)
post_save.connect(create_NI_user, sender=Lid)

# post_save.connect(events_add, sender=Event)
# post_save.connect(updateUser, sender=Lid)
# post_delete.connect(test1, sender=Event)
# Signal.connect(test1, sender=Event)