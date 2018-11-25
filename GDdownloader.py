from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import io
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

class GDdownloader():
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

    def download(self, file_id, file_name):
        request = self.service.files().get_media(fileId=file_id)
        #fh = io.BytesIO()
        #TODO get file name and type from metadata
        fh = io.FileIO(file_name, 'wb')
        downloader = MediaIoBaseDownload(fh, request, chunksize=1024*1024)

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
        return resp.get('name')

if __name__ == '__main__':
    dldr = GDdownloader()
    two_scoop_id = '1iSj4jp5wIvgBV0Pp6faGZyAdc4nf4aOW'
    filename = dldr.getMetadata(porn_id)
    dldr.download(porn_id, filename)


    
