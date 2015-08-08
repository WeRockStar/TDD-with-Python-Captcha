import unittest
from fizzbuzz import FizzBuzz

class TestToFizz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_it_should_return_fizz_when_is_3(self):
        self.assertEqual('Fizz' , self.fizzbuzz.count(3))

    def test_it_should_return_fizz_when_is_6(self):
        self.assertEqual('Fizz' , self.fizzbuzz.count(6))

class TestToBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_it_should_return_5_when_is_buzz(self):
        self.assertEqual('Buzz' , self.fizzbuzz.count(5))

    def test_it_should_return_buzz_when_is_10(self):
        self.assertEqual('Buzz' , self.fizzbuzz.count(10))

class TestNumberToString(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_it_should_return_1_when_is_1(self):
        self.assertEqual('1' , self.fizzbuzz.count(1))

    def test_it_should_return_2_when_is_2(self):
        self.assertEqual('2' , self.fizzbuzz.count(2))

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_it_should_return_fizzbuzz_when_is_15(self):
        self.assertEqual('FizzBuzz' , self.fizzbuzz.count(15))
