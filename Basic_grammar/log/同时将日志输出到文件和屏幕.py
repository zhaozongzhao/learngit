import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    filemode='w',
                    filename='日志1.txt',
                    datefmt='%a, %d %b %Y %H:%M:%S')

################################################################################################
#定义一个streamHandler,将INfo级别或更高的日志信息打印到标准错误,并将其添加到当前的日志处理对象
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter =  logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

################################################################################################

#日志回滚
#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
from logging.handlers import RotatingFileHandler
Rthandler = RotatingFileHandler('日志2.log',maxBytes=10*1024*1024,backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter =  logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)

################################################################################################


logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is debug message')
logging.error('this is error message')