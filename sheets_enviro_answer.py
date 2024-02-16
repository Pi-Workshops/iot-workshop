import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from sense_hat import SenseHat 
from time import sleep
import datetime

# --------- User Settings ---------
SHEETS_ID = "PLACE SHEETS ID HERE"
INPUT_SHEETS_RANGE = 'Sheet1!A1:C1000'
OUTPUT_SHEETS_RANGE_BASE = 'Sheet1!'
# ---------------------------------

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def find_empty_row(creds):
  try:
    # Call the Google API to open the Sheet
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEETS_ID,
                  range=INPUT_SHEETS_RANGE).execute()
    all_data = result.get('values', [])

    # Loop through all rows to find the first empty row
    for row_num in range(len(all_data)):
      if len(all_data[row_num]) <= 0:
        print("Row " + str(row_num+1) + " is the first empty row available for data")
        return row_num
      elif all_data[row_num][0] == '':
        print("Row " + str(row_num) + " is the first empty row available for data")
        return row_num
    print("Row " + str(row_num+1) + " is the first empty row available for data")
    return row_num+1

  except HttpError as err:
    return err

def update_values(row_num, temp_f, humidity, creds):
  try:
    # Call the Google API to open the Sheet
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    body = {
      'values': [[str(datetime.datetime.now()),str(temp_f),str(humidity)]]
    }
    print (body)
    # Calculate the Sheets output range based on row
    output_sheets_range = OUTPUT_SHEETS_RANGE_BASE + 'A' + str(row_num+1) + ':' + 'C' + str(row_num+1)
    result = service.spreadsheets().values().update(
      spreadsheetId=SHEETS_ID, range=output_sheets_range,
      valueInputOption="USER_ENTERED", body=body).execute()
    return result

  except HttpError as err:
    return err

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

  # Find first empty row to avoid overwriting any previous data
  row_num = find_empty_row(creds)

  # Get data from the Sense HAT
  sense = SenseHat()

  # Take temperature data until the script is killed
  while True:
    temp_c = sense.get_temperature()
    temp_f = format(temp_c * 9.0 / 5.0 + 32.0,".2f")
    humidity = format(sense.get_humidity(), ".2f")
    sense.show_message(temp_f)
    update_values(row_num, temp_f, humidity, creds)
    row_num += 1
    sleep(5)

if __name__ == '__main__':
  main()

