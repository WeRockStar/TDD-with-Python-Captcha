import unittest
from app import app
class TestCaptchaRounting(unittest.TestCase):
    def test_get_pattern(self):
        self.app = app.test_client()
        response = self.app.get('/captcha')
        self.assertEqual(response.status_code , 200)
        self.assertEqual('Fizz' , response.data)
