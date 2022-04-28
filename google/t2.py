import datetime
from datetime import timedelta

import pytz
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

service_account_email = "testcalendar@dispuutstropdas.iam.gserviceaccount.com"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    filename="client_secret.json", scopes=SCOPES
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
            calendarId="dev.gam.vollmer@gmail.com",
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