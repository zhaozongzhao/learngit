from selenium import  webdriver
import unittest
#运行文件夹绝对不要用test开始
#discover=找到指定目录下所有的测试模块，并可递归查到子文件下的测试模块
test_huijia='./'
discover=unittest.defaultTestLoader.discover(test_huijia,pattern='test*py')#要测试模块的目录，用例文件名的匹配原则

if __name__=='__main__':

    #构造测试集

    #执行测试

    runner = unittest.TextTestRunner()
    runner.run(discover)