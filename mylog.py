import logging
import os

LOG_FILE_NAME = 'log.txt'
FILTER_LOG = 'filter_log.txt'
TAG = 'pykTag'

def get_logger():
    logger = logging.getLogger(__name__)

    logging.basicConfig(filename=LOG_FILE_NAME,
                        format='%(asctime)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S',
                        level=logging.DEBUG,)


def log2file(func):
    logger = get_logger()
    def wrapper(*args, **kargs):
        get_logger()
        logging.warn('{}"{}" is running'.format(TAG, func.__name__))
        return func(*args, **kargs)
    return wrapper

@log2file
def testlog():
    for i in range(3+1):
        print('*'*i+'='*(3-i))

def filter_log():
    with open(LOG_FILE_NAME, 'r') as source:
        with open(FILTER_LOG, 'w') as des:
            for line in source.readlines():
                if TAG in line:
                    line = line.replace(TAG, '')
                    des.write(line[len(TAG):])

def clear_log():
    open(LOG_FILE_NAME, 'w').close()
    open(FILTER_LOG, 'w').close()

if __name__ == "__main__":
    testlog()

