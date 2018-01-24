import logging
import os
FILE = os.getcwd()
print(FILE)

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    filemode='w',
    filename=os.path.join(FILE,'log.txt'),
    datefmt='%a, %d %b %Y %H:%M:%S',
)
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.critical('This is warning message')
logging.error('This is warning message')


