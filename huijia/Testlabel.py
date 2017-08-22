from test import count
import unittest

class TestCount(unittest.TestCase):
  def setUp(self):
     print('开始')
  def test_add(self):
      j=count(2,3)
      self.assertEqual(j.add(),5,msg='值不相等')

  def test_add1(self):
      j=count(2,3)
      self.assertEqual(j.add(),6,msg='值不相等')

  def test_add2(self):
      j=count(3,3)
      self.assertEqual(j.add(),6,msg='值不相等')

  def tesrDown(self):
       print('结束')

if __name__=='__main__':
    suite=unittest.TestSuite()
    #构造测试集
    suite.addTest(TestCount('test_add1'))
    suite.addTest(TestCount('test_add2'))
    #执行测试
    runner = unittest.TextTestRunnert()
    runner.run(suite)
