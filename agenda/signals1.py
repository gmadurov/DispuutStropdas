import datetime
from datetime import timedelta

import pytz
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

service_account_email = "dispuutstropdas@dispuutstropdas.iam.gserviceaccount.com"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    filename="agenda/dispuutstropdas-e3544a721989.json", scopes=SCOPES
)


def build_service():
    service = build("calendar", "v3", credentials=credentials)
    return service


def create_event():
    service = build_service()

    start_datetime = datetime.datetime.now(tz=pytz.utc)
    event = (
        service.events()
        .insert(
            calendarId="12see8htsggg8dk2ng5j6j9vgs@group.calendar.google.com",
            body={
                "summary": "Foo",
                "description": "Bar",
                "start": {"dateTime": start_datetime.isoformat()},
                "end": {
                    "dateTime": (start_datetime + timedelta(minutes=15)).isoformat()
                },
            },
        )
        .execute()
    )

    print(event)


create_event()
