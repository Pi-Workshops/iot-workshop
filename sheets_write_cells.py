import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --------- User Settings ---------
SHEETS_ID = "PLACE SHEETS ID HERE"
SHEETS_RANGE = ''
TEST_DATA1 = "2024-02-13 13:37:15"
TEST_DATA2 = "85.6"
TEST_DATA3 = "30.96"
# ---------------------------------

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def main():

  # Authentication for Google APIs:
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  creds = None
  if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
      token.write(creds.to_json())

  try:
    # Call the Google API to open the Sheet
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    body = {
      'values': [[]]
    }
    print (body)
    result = service.spreadsheets().values().update(
      spreadsheetId=SHEETS_ID, range=SHEETS_RANGE,
      valueInputOption="USER_ENTERED", body=body).execute()
    print(result)

  except HttpError as err:
    print(err)

if __name__ == '__main__':
  main()

