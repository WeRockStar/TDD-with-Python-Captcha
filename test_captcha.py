import unittest
from captcha import Captcha

class TestFirstPatternLeftOperland(unittest.TestCase):
    def test_1_should_1(self):
        captcha = Captcha(1,1,1,1)
        self.assertEqual(1 , captcha.left)
