from __future__ import print_function

import datetime
import json
import os.path
from pathlib import Path
from pprint import pprint

from django.contrib import messages
from django.db.models.signals import post_delete, post_save
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from users.models import Lid

from .models import AgendaClient, Event, NIEvent

# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/calendar']
# SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events','https://www.googleapis.com/auth/calendar.events.readonly','https://www.googleapis.com/auth/calendar.readonly']
try:
    SCOPES = (AgendaClient.objects.get(name='SCOPES').json).strip("][").split(', ')
except: pass
def get_service(refresh = False):
    '''this functions gets and builds the service using the token and the client_secret'''
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if len(AgendaClient.objects.filter(name='token'))==1:
            creds = Credentials.from_authorized_user_info(json.loads(AgendaClient.objects.get(name='token').json), SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(
                    json.loads(AgendaClient.objects.get(name='client_secret').json), SCOPES)
            creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    AgendaClient.objects.update_or_create(name='token', defaults = {'json':creds.to_json()})
    if not refresh:
        service = build('calendar', 'v3', credentials=creds)
        return service
    
def handle_event(sender,created, instance=None,  **kwargs):
    """this function creates the events in the google agenda and updates them if changed in the website
    """
    service = get_service()
    evs = instance
    event ={
    'summary': evs.description,
    'location': evs.location or "",
    'description': (evs.description+' '+ evs.summary),
    'start': {
        'dateTime': datetime.datetime.combine(evs.start_date,evs.start_time).isoformat(),
        'timeZone': 'Europe/Amsterdam',
    },
    'end': {
        'dateTime':datetime.datetime.combine(evs.end_date,evs.end_time).isoformat() ,
        'timeZone': 'Europe/Amsterdam',
    },
    'recurrence': [],'reminders': {}}

    if created or not instance.google_link:
        try:
            event = service.events().insert(calendarId=AgendaClient.objects.get(name='calendarId').json, body=event).execute()
            instance.google_link = event['id']
            instance.save()
        except HttpError as error:
            print('An error occurred: %s' % error)
            pass
    else:  
        try:
            # print(type(AgendaClient.objects.get(name='calendarId').json))
            event = service.events().update(calendarId=AgendaClient.objects.get(name='calendarId').json, body=event, eventId = instance.google_link).execute()
        except HttpError as error:
            print('An error occurred: %s' % error)
            pass

def delete_event(sender, instance,  **kwargs):
    '''this function deletes an event from google agenda whendeleted in the website'''
    try:
        service = get_service()
        service.events().delete(calendarId=AgendaClient.objects.get(name='calendarId').json, eventId=instance.google_link ).execute()
        # messages.info('Deleting event from google agenda')
    except:
        pass
        # messages.info('Failed to delete event from google agenda')

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


post_save.connect(create_NI_event, sender=Event)
post_save.connect(create_NI_user, sender=Lid)

post_save.connect(handle_event, sender=Event)
post_delete.connect(delete_event, sender=Event)
