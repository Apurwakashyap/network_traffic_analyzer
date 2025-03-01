import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Load OAuth2 token
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


creds = Credentials.from_authorized_user_file("token.json", SCOPES)

def send_email(subject, body, to_email):
    try:
        service = build("gmail", "v1", credentials=creds)

        # Create email message
        message = MIMEText(body)
        message["to"] = to_email
        message["subject"] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        # Send email
        service.users().messages().send(userId="me", body={"raw": raw_message}).execute()
        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Error sending email:", str(e))

if __name__ == "__main__":
    send_email("🚨 Network Threat Detected!", "Suspicious activity found in network logs.", "apurwa1909@gmail.com")
