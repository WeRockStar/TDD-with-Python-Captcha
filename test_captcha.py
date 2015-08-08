import unittest
from captcha import Captcha,SecordPatternOperland

OPERAND = 1
RIGTH = 1
LEFT = 1

class TestFirstPatternLeftOperand(unittest.TestCase):
    def setUp(self):
        self.first_pattern = 1

    def test_1_should_1(self):
        captcha = Captcha(self.first_pattern , 1 , OPERAND , RIGTH)
        self.assertEqual('1' , captcha.leftOperator())

    def test_2_should_2(self):
        captcha = Captcha(self.first_pattern , 2 , OPERAND , RIGTH)
        self.assertEqual('2' , captcha.leftOperator())

class TestSecondPatternLeftOperand(unittest.TestCase):
    def setUp(self):
        self.second_pattern = 2

    def test_1_should_One(self):
        leftCaptcha = SecordPatternOperland(self.second_pattern , 1 , OPERAND , RIGTH)
        self.assertEqual('One' , leftCaptcha.leftOperator())

    def test_2_should_Two(self):
        leftCaptcha = SecordPatternOperland(self.second_pattern , 2 , OPERAND , RIGTH)
        self.assertEqual('Two' , leftCaptcha.leftOperator())

class TestSecondPatternRigthOperand(unittest.TestCase):
    def setUp(self):
        self.second_pattern = 2

    def test_1_should_One(self):
        rigthCaptcha = SecordPatternOperland(self.second_pattern , LEFT , OPERAND , 1)
        self.assertEqual('One' , rigthCaptcha.rightOperator())

    def test_2_should_Two(self):
        rigthCaptcha = SecordPatternOperland(self.second_pattern , LEFT , OPERAND , 2)
        self.assertEqual('Two' , rigthCaptcha.rightOperator())
