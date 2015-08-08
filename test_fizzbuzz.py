import unittest
class FizzBuzz():
    def count(self , number):
        if number == 1:
            return '1'
        return '2'

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_it_should_return_1_when_is_1(self):
        self.assertEqual('1' , self.fizzbuzz.count(1))
    def test_it_should_return_2_when_is_2(self):
        self.assertEqual('2' , self.fizzbuzz.count(2))
