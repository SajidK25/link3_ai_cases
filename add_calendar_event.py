"""
Google Calendar Event Creator
Run this script after placing your credentials.json file in the same directory.
"""
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def add_event():
    """Adds a test event to Google Calendar."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("ERROR: credentials.json not found!")
                print("\nPlease follow these steps:")
                print("1. Go to https://console.cloud.google.com/")
                print("2. Create a new project (or select existing)")
                print("3. Enable the Google Calendar API")
                print("4. Go to APIs & Services > Credentials")
                print("5. Click 'Create Credentials' > 'OAuth client ID'")
                print("6. Application type: Desktop app")
                print("7. Download the JSON file and save it as 'credentials.json' in this folder")
                print("\nThen run this script again.")
                return
            
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Calculate tomorrow's date at 8:00 AM Asia/Dhaka time
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        
        # Create ISO format datetime strings
        start_time = f"{tomorrow.isoformat()}T08:00:00+06:00"
        end_time = f"{tomorrow.isoformat()}T09:00:00+06:00"

        event = {
            'summary': 'test event',
            'description': 'Event created via Python script',
            'start': {
                'dateTime': start_time,
                'timeZone': 'Asia/Dhaka',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'Asia/Dhaka',
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"✅ Event created successfully!")
        print(f"   Title: {event.get('summary')}")
        print(f"   Start: {event.get('start', {}).get('dateTime')}")
        print(f"   Link: {event.get('htmlLink')}")

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    add_event()
