from __future__ import print_function
import os
import re
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_folder_id(folder_link):
    """Extract folder ID from a shared Google Drive folder link"""
    match = re.search(r'/folders/([a-zA-Z0-9_-]+)', folder_link)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid folder link!")

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    folder_link = input("Paste your Google Drive folder link: ").strip()
    folder_id = get_folder_id(folder_link)

    query = f"'{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, pageSize=1000, fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print("No files found in this folder.")
    else:
        print(f"Found {len(items)} files. Saving to drive_file_list.txt ...")
        with open('drive_file_list.txt', 'w') as f:
            for item in items:
                file_id = item['id']
                name = item['name']
                direct_link = f"https://drive.google.com/uc?id={file_id}"
                f.write(f"{name} | {file_id} | {direct_link}\n")
        print("Done! Check drive_file_list.txt for all file IDs and links.")

if __name__ == "__main__":
    main()

