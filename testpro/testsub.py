from count import count
import unittest

class Mytest(unittest.TestCase):
     def setUp(self):
      print('开始')

     def tesrDown(self):
       print('结束')

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
