import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --------- User Settings ---------
SHEETS_ID = "PLACE SHEETS ID HERE"
SHEETS_RANGE = 'Sheet1!A1:Z1000'
# ---------------------------------

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def col(col_letter):
  if col_letter == 'A': 
    return 0
  elif col_letter == 'B': 
    return 1
  elif col_letter == 'C': 
    return 2
  elif col_letter == 'D': 
    return 3   
  elif col_letter == 'E': 
    return 4   
  elif col_letter == 'F': 
    return 5   
  elif col_letter == 'G': 
    return 6   
  elif col_letter == 'H': 
    return 7   
  elif col_letter == 'I': 
    return 8   
  elif col_letter == 'J': 
    return 9   
  elif col_letter == 'K': 
    return 10   
  elif col_letter == 'L': 
    return 11   
  elif col_letter == 'M': 
    return 12   
  elif col_letter == 'N': 
    return 13   
  elif col_letter == 'O': 
    return 14   
  elif col_letter == 'P': 
    return 15   
  elif col_letter == 'Q': 
    return 16   
  elif col_letter == 'R': 
    return 17   
  elif col_letter == 'S': 
    return 18   
  elif col_letter == 'T': 
    return 19   
  elif col_letter == 'U': 
    return 20   
  elif col_letter == 'V': 
    return 21   
  elif col_letter == 'W': 
    return 22   
  elif col_letter == 'X': 
    return 23   
  elif col_letter == 'Y': 
    return 24   
  elif col_letter == 'Z': 
    return 25   

def row(row_num):
  return row_num - 1

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

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SHEETS_ID, range=SHEETS_RANGE)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    # Read a single cell and print its value
    cell_value = values[row(4)][col('C')]
    print(cell_value)

  except HttpError as err:
    print(err)

if __name__ == '__main__':
  main()

