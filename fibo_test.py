import unittest
from fibo import Fibo


class FiboTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(Fibo(10).cal_fibo(), 55)

    def test2(self):
        self.assertEqual(Fibo(20).cal_fibo(), 6765)

    def test3(self):
        self.assertEqual(Fibo(30).cal_fibo(), 832040)

    def test4(self):
        self.assertEqual(Fibo(35).cal_fibo(), 9227465)

    def test5(self):
        self.assertEqual(Fibo(15).cal_fibo() - Fibo(10).cal_fibo(), 555)
