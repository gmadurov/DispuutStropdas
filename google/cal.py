# from __future__ import print_function

import datetime
import json
import os.path

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from httplib2 import Http
import pytz
from requests.structures import CaseInsensitiveDict

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials



def get_credentials():
    SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events','https://www.googleapis.com/auth/calendar.events.readonly','https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
            creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('/home/gmadurov/websitebullshits/DispuutStropdas/google/client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
    return creds 
def get_events(creds):
    service = build('calendar', 'v3', credentials = creds)
    now = datetime.datetime.utcnow().isoformat()+'Z'
    events = service.events().list(calendarId = 'primary', timeMin = now, singleEvents = True, orderBy = 'startTime').execute()
    with open('events.json', 'w') as file:
        file.write(json.dumps((events)))
    print(events)   
# get_credentials()
    
# def create(creds):
    # service_account_email = "testcalendar@dispuutstropdas.iam.gserviceaccount.com"
    # creds = creds.refresh(Request())

def build_service(credentials):
    service = build("calendar", "v3", credentials=credentials)
        # service = build("calendar", "v3",http = credentials.authorize(Http()))
    return service


def create_event(credentials):
    service = build_service(credentials)

    start_datetime = datetime.datetime.now(tz=pytz.utc)
    event = (
        service.events()
        .insert(
            calendarId="dev.gam.vollmer@gmail.com", sendNotification = True,
            body={
                "summary": "test-gus",
                "description": "testing the creat script",
                "start": {"dateTime": start_datetime.isoformat()},
                "end": {
                    "dateTime": (start_datetime + datetime.timedelta(minutes=15)).isoformat()
                },
            },
        )
        .execute()
    )

    print(f'''{event[ 'summary' ]} added:
    
    start: {event[ 'start' ]} 
    end: {event[ 'end']}''')
    
create_event(get_credentials())

# if __name__ == '__main__':
#     creds = (get_credentials())