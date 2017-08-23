from selenium import  webdriver
from count import count
import unittest
import testadd
import testsub


#  unittest.main()
'''class Mytest(unittest.TestCase):
     def setUp(self):
      print('开始')

     def tesrDown(self):
       print('结束')

class Testadd(Mytest):

  def test_add(self):
      j=count(2,3)
      self.assertEqual(j.add(),5,msg='值不相等')

  def test_add1(self):
      j=count(2,3)
      self.assertEqual(j.add(),6,msg='值不相等')

  def test_add2(self):
      j=count(3,3)
      self.assertEqual(j.add(),6,msg='值不相等')

class Testsub(Mytest):

  def test_sub(self):
      j=count(2,3)
      self.assertEqual(j.sub(),5,msg='值不相等')

  def test_sub1(self):
      j=count(2,3)
      self.assertEqual(j.sub(),-1,msg='值不相等')

  def test_sub2(self):
      j=count(3,3)
      self.assertEqual(j.sub(),6,msg='值不相等')
      '''
suite=unittest.TestSuite()
suite.addTest(testadd.Testadd('test_add2'))
suite.addTest(testadd.Testadd('test_add1'))
suite.addTest(testadd.Testadd('test_add'))
suite.addTest(testsub.Testsub('test_sub'))
suite.addTest(testsub.Testsub('test_sub1'))
suite.addTest(testsub.Testsub('test_sub2'))




'''huijiar='C:\\Users\\zzz\\learngit\\huijia'
discover=unittest.defaultTestLoader.discover(huijiar,pattern='test*py')'''

if __name__=='__main__':

    #构造测试集

    #执行测试

    runner = unittest.TextTestRunner()
    runner.run(suite)