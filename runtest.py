from selenium import  webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
#运行文件夹绝对不要用test开始
#discover=找到指定目录下所有的测试模块，并可递归查到子文件下的测试模块
test_huijia='C:\\Users\\zzz\\learngit\\test_CheckDoctor'
discover=unittest.defaultTestLoader.discover(test_huijia,pattern='test*py')#要测试模块的目录，用例文件名的匹配原则

if __name__=='__main__':

    now=time.strftime('%Y-%m-%d %H-%m-%M')
    #定位用例存放位置
    fp=open("result"+now+".html",'wb')
    #
    runner=HTMLTestRunner(stream=fp,title='测试报告',description=u'用例执行情况:')
    runner.run(discover)
    fp.close()




