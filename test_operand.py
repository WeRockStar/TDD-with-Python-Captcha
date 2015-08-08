import unittest
from operand import Operand , OperandString , OperandNumber

class TestOperandString(unittest.TestCase):
    def test_1_should_One(self):
        operandStr = OperandString(1)
        self.assertEqual('One' , operandStr.toString())

    def test_2_should_Two(self):
        operandStr = OperandString(2)
        self.assertEqual('Two' , operandStr.toString())

class TestOperandNumber(unittest.TestCase):
    def test_1_should_2(self):
        operandNum = OperandNumber(1)
        self.assertEqual(1 , operandNum.toString())

    def test_2_should_2(self):
        operandNum = OperandNumber(2)
        self.assertEqual(2 , operandNum.toString())
