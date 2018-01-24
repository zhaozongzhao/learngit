
import logging

def fun():
   logging.basicConfig(level=logging.DEBUG,
                    # format='%(filename)s[line:%(lineno)d] %(levelname) %(message)s',
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='11.log',
                    filemode='w')

   logging.info('util module start')
   logging.error('util module stop')

if __name__ == '__main__':
    fun()