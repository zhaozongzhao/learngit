# threading的Timer：
#
# threading模块中的Timer能够帮助实现定时任务，而且是非阻塞的。
#
# 比如3秒后打印helloworld：

from threading import Timer

def printHello():
    print( "Hello World"  )
    t = Timer(10, printHello)
    t.start()


if __name__ == "__main__":
    printHello()