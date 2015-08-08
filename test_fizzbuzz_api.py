import unittest
from app import app
class TestRounting(unittest.TestCase):
    def test_fail(self):
        self.app = app.test_client()
        response = self.app.get('/')
        self.assertEqual(response.status_code , 200)
        self.assertEqual('Hello Flask' , response.data)

    def test_3_fizz(self):
        self.app = app.test_client()
        response = self.app.get('/fizzbuzz/3')
        self.assertEqual(response.status_code , 200)
        self.assertEqual('Fizz' , response.data)

    def test_5_fizz(self):
        self.app = app.test_client()
        response = self.app.get('/fizzbuzz/5')
        self.assertEqual(response.status_code , 200)
        self.assertEqual('Buzz' , response.data)

    def test_15_fizz(self):
        self.app = app.test_client()
        response = self.app.get('/fizzbuzz/15')
        self.assertEqual(response.status_code , 200)
        self.assertEqual('FizzBuzz' , response.data)
