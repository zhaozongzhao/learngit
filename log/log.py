import logging



###############################################日志的输入内容#############################################
# logging.basicConfig(level=logging.DEBUG,
#                     # format='%(filename)s[line:%(lineno)d] %(levelname) %(message)s',
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='11.log',
#                     filemode='w')

# logging.basicConfig函数各参数:
# filename: 指定日志文件名
# filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
# format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
#  %(levelno)s: 打印日志级别的数值
#  %(levelname)s: 打印日志级别名称
#  %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
#  %(filename)s: 打印当前执行程序名
#  %(funcName)s: 打印日志的当前函数
#  %(lineno)d: 打印日志的当前行号
#  %(asctime)s: 打印日志的时间
#  %(thread)d: 打印线程ID
#  %(threadName)s: 打印线程名称
#  %(process)d: 打印进程ID
#  %(message)s: 打印日志信息
# datefmt: 指定时间格式，同time.strftime()
# level: 设置日志级别，默认为logging.WARNING
# stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
#*********************************************************************************************************************
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#

#创建一个日志记录器
logger = logging.getLogger()
logger.setLevel(logging.WARNING)            #log等级开关


#第二部创建一个handler，用于写入日志文件
logfile = '12.txt'
fh = logging.FileHandler(logfile,mode='w')
fh.setLevel(logging.ERROR)                 #输出到file的等级开关

#第三部 ，创建一个handler ，用于输出到控制台c
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

#第四步
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#将logger添加到处理程序
logger.addHandler(fh)
logger.addHandler(ch)



def main():
    logger.debug('This is debug message')
    logger.info('This is info message')
    logging.warning('This is warning message')
    logger.critical('This is warning message')
    logger.error('This is warning message')

if __name__ == '__main__':
    main()



