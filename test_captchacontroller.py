import unittest
from captchacontroller import CaptchaController

class TestController(unittest.TestCase):
    def test_get_json_1(self):
        json = CaptchaController()
        jsonExpect = '{\'left\':1 , \'operand\':1 , \'right\' : 1}'
        self.assertEqual(jsonExpect , json.getJson('1'))

    def test_get_json_2(self):
        json = CaptchaController()
        jsonExpect = '{\'left\':2 , \'operand\':1 , \'right\' : 1}'
        self.assertEqual(jsonExpect , json.getJson('2'
        ))
