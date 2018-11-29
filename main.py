import os
import GDdownloader
import mylog

def test():
    test_jpg = '0B3Y1tx84rF9sTHhGOWdoNEh2Nms'

    dldr = GDdownloader.GDdownloader()
    filename = dldr.getMetadata(test_jpg)
    dldr.download(test_jpg, filename)


mylog.clear_log()
test()
mylog.filter_log()