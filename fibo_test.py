import unittest
from fibo import Fibo


class FiboTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(Fibo(10).cal_fibo(), 55)

    def test2(self):
        self.assertEqual(Fibo(20).cal_fibo(), 6765)

    def test3(self):
        self.assertEqual(Fibo(30).cal_fibo(), 832040)

