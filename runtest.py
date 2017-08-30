from selenium import  webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
#运行文件夹绝对不要用test开始
#discover=找到指定目录下所有的测试模块，并可递归查到子文件下的测试模块
test_huijia='C:\\Users\\zzz\\learngit\\test_huijia'
discover=unittest.defaultTestLoader.discover(test_huijia,pattern='test*py')#要测试模块的目录，用例文件名的匹配原则

if __name__=='__main__':

    #构造测试集
    now=time.strftime('%Y-%m-%d')
      #打开一个文件，将result写入此file中
    fp=open("result"+now+".html",'wb')
    runner=HTMLTestRunner(stream=fp,title='test result',description=u'result:')
    runner.run(discover)
    fp.close()

    #runner = unittest.TextTestRunner()
    #runner.run(discover)



