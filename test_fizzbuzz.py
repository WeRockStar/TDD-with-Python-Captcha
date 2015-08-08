import unittest
class FizzBuzz():
    def count(self , number):
        return 1

class TestFizzBuzz(unittest.TestCase):
    def test_it_should_return_1_when_is_1(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(1 , fizzbuzz.count(1))
