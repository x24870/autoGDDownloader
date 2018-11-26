import logging

LOG_FILE_NAME = 'log.txt'
FILTER_LOG = 'filter_log.txt'
TAG = '***'

root = logging.getLogger(__name__)

logging.basicConfig(filename=LOG_FILE_NAME,
                    format=TAG+'%(asctime)s %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    level=logging.DEBUG,)


def log2file(func):
    def wrapper():
        logging.warn('"{}" is running'.format(func.__name__))
        return func
    return wrapper()

@log2file
def testlog():
    for i in range(3+1):
        print('*'*i, '='*(3-i))

def filter_log():
    with open(LOG_FILE_NAME, 'r') as source:
        with open(FILTER_LOG, 'w') as des:
            for line in source.readlines():
                if line.startswith(TAG):
                    des.write(line[len(TAG):])

if __name__ == "__main__":
    filter_log()

