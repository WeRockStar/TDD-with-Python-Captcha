import unittest
from operators import Operator

class TestOperator(unittest.TestCase):
    def test_1_should_Plus(self):
        operator = Operator(1)
        self.assertEqual('+' , operator.toString())

    def test_2_should_Sub(self):
        operator = Operator(2)
        self.assertEqual('-' , operator.toString())

    def test_3_should_Mul(self):
        operator = Operator(3)
        self.assertEqual('*' , operator.toString())
