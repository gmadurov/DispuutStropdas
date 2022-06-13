from datetime import datetime, time
import json

# import time
from django.db.models.signals import post_delete, post_save
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from users.models import Lid

from .models import AgendaClient, Event, NIEvent

# If modifying these scopes, delete the file token.json.

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
    event = instance
    if not event.end_date:
        event.end_date = event.start_date
    if not event.start_time:
        event.start_time = time(15, 0)
    if not event.end_time:
        event.end_time = time(23, 59, 0)
    if event.end_date < event.start_date:
        event.end_date, event.start_date = event.start_date, event.end_date
    queryset = Event.objects.filter(
        id=event.id
    )  # https://stackoverflow.com/questions/1555060/how-to-save-a-model-without-sending-a-signal
    # this is used so that we can update the google event within this signal without reshooting this signal(signals shot every time an object is saved)
    kokers = ""
    for koker in event.kokers.all():
        kokers += koker.initials + " "
    event_body = {
        "summary": event.description,
        "location": event.location or "",
        "description": f"{event.description} ({event.summary}) \n{'Kokers: '+ (kokers) if event.kokers else ''}\n{'Kartrekkers: '+event.kartrekkers if event.kartrekkers else ''}\n{'Bijsonderheiden: '+event.bijzonderheden if event.bijzonderheden else ''}\n{'Extra info: '+event.info if event.info else ''}",
        "start": {
            "dateTime": datetime.combine(
                event.start_date, event.start_time
            ).isoformat(),
            "timeZone": "Europe/Amsterdam",
        },
        "end": {
            "dateTime": datetime.combine(event.end_date, event.end_time).isoformat(),
            "timeZone": "Europe/Amsterdam",
        },
        "recurrence": [],
        "reminders": {},
    }

    if created or not instance.google_link:
        try:
            google_event = (
                service.events()
                .insert(
                    calendarId=AgendaClient.objects.get(name="calendarId").json,
                    body=event_body,
                )
                .execute()
            )
            queryset.update(
                google_link=google_event["id"],
                start_date=event.start_date,
                start_time=event.start_time,
                end_date=event.end_date,
                end_time=event.end_time,
            )

        except HttpError as error:
            print("An error occurred:1 %s" % error)
            pass
    else:
        try:
            google_event = (
                service.events()
                .update(
                    calendarId=AgendaClient.objects.get(name="calendarId").json,
                    body=event_body,
                    eventId=event.google_link,
                )
                .execute()
            )
            queryset.update(
                google_link=google_event["id"],
                start_date=event.start_date,
                start_time=event.start_time,
                end_date=event.end_date,
                end_time=event.end_time,
            )

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
