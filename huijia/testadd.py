import unittest
from test import count
class Mytest(unittest.TestCase):
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
