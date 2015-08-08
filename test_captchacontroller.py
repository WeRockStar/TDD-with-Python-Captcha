import unittest
from captchacontroller import CaptchaController

class TestController(unittest.TestCase):
    def isJson(self):
        json = CaptchaController()
        jsonExpect = "{\'left\':1 , \'operand\':1 , \'right\' : 1}"
        self.assertEqual(json , json.toJson())
