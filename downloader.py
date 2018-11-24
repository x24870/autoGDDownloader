from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import io
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

class downloader():
    def __init__(self):
        self.service = self.build_service()

    def build_service(self):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        drive_service = build('drive', 'v3', http=creds.authorize(Http()))

        return drive_service

    def download(self, file_id):
        request = self.service.files().get_media(fileId=file_id)
        #fh = io.BytesIO()
        #TODO get file name and type from metadata
        fh = io.FileIO('test3.jpg', 'wb')
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

        return

    def searchPrefix(self, name):
        query = "name contains '{}'".format(name)
        resp = self.service.files().list(q=query).execute()
        for i in resp.get('files', []):
            print(i)

    def getMetadata(self, id):
        resp = self.service.files().get(fileId=id).execute()
        print(resp.get('name'))

if __name__ == '__main__':
    dldr = downloader()
    #dldr.download('0B3Y1tx84rF9sd0QtT0NuTGJkT0U')
    #dldr.searchPrefix('')
    dldr.getMetadata('1AdsGVVHdFfmFl3_vd4HVBN_coHZ1RFSg')
    
