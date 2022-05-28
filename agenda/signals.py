from __future__ import print_function

import datetime
import json
import os.path
from datetime import timedelta
from pathlib import Path
from pprint import pprint

import pytz
from django.contrib import messages
from django.db.models.signals import post_delete, post_save
from google.auth.transport.requests import Request
from google.cloud import storage
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from users.models import Lid

from .models import AgendaClient, Event, NIEvent

# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/calendar']
# SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events','https://www.googleapis.com/auth/calendar.events.readonly','https://www.googleapis.com/auth/calendar.readonly']
try:
    SCOPES = (AgendaClient.objects.get(name="SCOPES").json).strip("][").split(", ")
except:
    pass


def get_service(refresh=False):
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        json.loads(AgendaClient.objects.get(name="client_secret").json), scopes=SCOPES
    )

    service = build("calendar", "v3", credentials=credentials)
    return service


def handle_event(sender, created, instance, **kwargs):
    """this function creates the events in the google agenda and updates them if changed in the website"""
    service = get_service()
    evs = instance
    queryset = Event.objects.filter(id=evs.id) # https://stackoverflow.com/questions/1555060/how-to-save-a-model-without-sending-a-signal
    # this is used so that we can update the google event within this signal without reshooting this signal(signals shot every time an object is saved)
    event = {
        "summary": evs.description,
        "location": evs.location or "",
        "description": (evs.description + " " + evs.summary),
        "start": {
            "dateTime": datetime.datetime.combine(
                evs.start_date, evs.start_time
            ).isoformat(),
            "timeZone": "Europe/Amsterdam",
        },
        "end": {
            "dateTime": datetime.datetime.combine(
                evs.end_date, evs.end_time
            ).isoformat(),
            "timeZone": "Europe/Amsterdam",
        },
        "recurrence": [],
        "reminders": {},
    }

    if created or not instance.google_link:
        try:
            event = (
                service.events()
                .insert(
                    calendarId=AgendaClient.objects.get(name="calendarId").json,
                    body=event,
                )
                .execute()
            )
            queryset.update(google_link=event["id"])
        except HttpError as error:
            print("An error occurred:1 %s" % error)
            pass
    else:
        try:
            event = (
                service.events()
                .update(
                    calendarId=AgendaClient.objects.get(name="calendarId").json,
                    body=event,
                    eventId=instance.google_link,
                )
                .execute()
            )
            queryset.update(google_link=event["id"])
        except HttpError as error:
            print("An error occurred:2 %s" % error)
            pass


def delete_event(sender, instance, **kwargs):
    """this function deletes an event from google agenda whendeleted in the website"""
    try:
        service = get_service()
        service.events().delete(
            calendarId=AgendaClient.objects.get(name="calendarId").json,
            eventId=instance.google_link,
        ).execute()
    except:
        pass


def create_NI_event(sender, instance, created, **kwargs):
    """creates NI events when a new event is created"""
    if created:
        leden = Lid.objects.filter(active=True)
        even = instance
        for li in leden:
            ni = NIEvent.objects.create(
                event=even,
                points=0,
                lid=li,
                note="",
            )


def create_NI_user(sender, instance, created, **kwargs):
    """creates NI events when a new profile is created"""
    # if created:
    Events = Event.objects.all()
    lid = instance.user.lid
    for lid in Lid.objects.filter(active=True):
        for ev in Events:
            ni = NIEvent.objects.create(
                event=ev,
                points=0,
                lid=lid,
                note="",
            )


post_save.connect(create_NI_event, sender=Event)
post_save.connect(create_NI_user, sender=Lid)

post_save.connect(handle_event, sender=Event)
post_delete.connect(delete_event, sender=Event)
