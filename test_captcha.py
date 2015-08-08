import unittest
from captcha import Captcha,SecordPatternOperland

class TestFirstPatternLeftOperand(unittest.TestCase):
    def setUp(self):
        self.first_pattern = 1
        self.left = 1
        self.op = 1
        self.rigth = 1

    def test_1_should_1(self):
        captcha = Captcha(self.first_pattern , 1 , self.op , self.rigth)
        self.assertEqual('1' , captcha.leftOperator())

    def test_2_should_2(self):
        captcha = Captcha(self.first_pattern , 2 , self.op , self.rigth)
        self.assertEqual('2' , captcha.leftOperator())

class TestSecondPatternLeftOperand(unittest.TestCase):
    def setUp(self):
        self.second_pattern = 2
        self.op = 1
        self.rigth = 1

    def test_1_should_One(self):
        leftCaptcha = SecordPatternOperland(self.second_pattern , 1 , self.op , self.rigth)
        self.assertEqual('One' , leftCaptcha.leftOperator())

    def test_2_should_Two(self):
        leftCaptcha = SecordPatternOperland(self.second_pattern , 2 , self.op , self.rigth)
        self.assertEqual('Two' , leftCaptcha.leftOperator())
