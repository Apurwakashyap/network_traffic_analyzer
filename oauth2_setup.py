from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

# Define OAuth2 scope for Gmail API
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def authenticate_gmail():
    creds = None

    # Check if token file exists
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If no valid credentials, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save token for future use
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    print("✅ OAuth2 Authentication Successful! Token saved as 'token.json'.")

if __name__ == "__main__":
    authenticate_gmail()
