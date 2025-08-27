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

```bash
python3 -m venv venv
