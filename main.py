import os
import GDdownloader

from mylog import log2file, filter_log

#TODO: download to specified path

URL_FILE = 'urls.txt'
DOWNLOAD_FOLDER = 'download'

def test():
    '''
    Download a jpg file and log to file
    '''
    test_jpg = '0B3Y1tx84rF9sTHhGOWdoNEh2Nms'

    dldr = GDdownloader.GDdownloader()
    filename = dldr.getMetadata(test_jpg)
    dldr.download(test_jpg, filename)

    mylog.filter_log()

@log2file
def get_urls():
    file_id_list = []
    try:
        f = open(URL_FILE, 'r')
    except FileNotFoundError:
        #TODO: log2file
        print("[Error] Can't find {}".format(URL_FILE))
        return

    for line in f.readlines():
        try:
            file_id_list.append(line.split('id=')[1][:-1])
        except:
            #TODO: log2file
            print('Invalid url{}'.format(line))


    f.close()

    return file_id_list

def download_files(file_id_list):
    #Get service
    dldr = GDdownloader.GDdownloader()

    for file_id in file_id_list:
        filename = dldr.getMetadata(file_id)
        dldr.download(file_id, filename)

    mylog.filter_log()

def update_url_file():
    #TODO: update url file, seperate to successed and failed
    pass


if __name__ == "__main__":
    file_id_list = get_urls()
    download_files(file_id_list)

    filter_log()