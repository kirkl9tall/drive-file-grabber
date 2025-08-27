# Google Drive File ID Extractor

A Python script that lists all files in a Google Drive folder, extracts their file IDs, and generates direct download links. Outputs a ready-to-use text file with file names, IDs, and links.

---

## ⚠️ Important
- You **must provide your own `credentials.json`** (OAuth client) from Google Cloud Console.  
- Do **not commit sensitive credentials** to public repositories.  

---

## Features
- Lists all files in a shared Google Drive folder.  
- Extracts file names and IDs.  
- Generates direct download links (`https://drive.google.com/uc?id=FILE_ID`).  
- Saves output in `drive_file_list.txt`.  

---

## Setup

### 1. Create a Google Cloud Project & OAuth Credentials
1. Go to [Google Cloud Console](https://console.developers.google.com/).  
2. Create a new project.  
3. Enable **Google Drive API** for this project.  
4. Go to **Credentials → Create Credentials → OAuth Client ID → Desktop App**.  
5. Download the JSON file and save it as `credentials.json` in your project folder.  

---

### 2. Set up Python Environment
1. Install Python 3.12 (or compatible version).  
2. Create a virtual environment:


python3 -m venv venv
Activate the virtual environment:

source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


Install required packages:
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
3. Run the Script

Make sure credentials.json is in the project folder.

Run the script:
```bash
python3 list_drive_files.py
```

Paste your shared Google Drive folder link when prompted.

Authorize access in your browser when prompted.

After successful authentication, a file drive_file_list.txt will be generated with all file names, IDs, and direct links.

4. Output Example
```bash
76.webp | 189w1O4TAFveDGJtktNTa4dFPaA0RHKOG | https://drive.google.com/uc?id=189w1O4TAFveDGJtktNTa4dFPaA0RHKOG
86.webp | 1eoMbsIg-mkfTmJRcL7V10pnZySAbTtVB | https://drive.google.com/uc?id=1eoMbsIg-mkfTmJRcL7V10pnZySAbTtVB
52.webp | 1uUflPEWjs4e62BbRU4jTnUdxClSdiaUA | https://drive.google.com/uc?id=1uUflPEWjs4e62BbRU4jTnUdxClSdiaUA
...
```
6. Notes

If your folder has subfolders, you may need to adjust the script to recursively list files.

Keep your token.json safe; it stores your OAuth access token.

You can edit the script to change output formatting or include additional file metadata.

6. Usage as a Module / API

You can also import the main functions from list_drive_files.py in another Python script and call them directly with a folder ID:

from list_drive_files import get_drive_files

folder_id = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
files = get_drive_files(folder_id)
for f in files:
    print(f"{f['name']} | {f['id']} | https://drive.google.com/uc?id={f['id']}")


This allows integration into other Python projects or automation scripts.

7. License
```bash
MIT License – feel free to use, modify, and share.
```

I can also **make a shorter version with badges, installation, and usage sections** so it looks professional on GitHub. Do you want me to do that too?

