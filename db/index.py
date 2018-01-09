import tkinter
import tkinter.messagebox
import sys
sys.setrecursionlimit(1500)
from threading import Timer

def mian():

   print('开始')
   root = tkinter.Tk()
   top = tkinter
   top.messagebox.askokcancel('提示', '存在患者需要处理')
   root.destroy()
   print('结束')
   t = Timer(10, mian)
   t.start()



# def printHello():
#     print( "Hello World"  )
#     t = Timer(10, printHello)
#     t.start()
#
#
# if __name__ == "__main__":
#     printHello()


if __name__ == "__main__":
    mian()