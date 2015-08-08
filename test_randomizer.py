import unittest
from randomizers import Randomizer
class TestRandomizer(unittest.TestCase):
    def test_pattern(self):
        rand = Randomizer()
        self.assertIn(rand.getPattern() , [1,2])

    def test_operand(self):
        rand = Randomizer()
        self.assertIn(rand.getOperand() , [1,9])

    def test_operator(self):
        rand = Randomizer()
        self.assertIn(rand.getOperator() , [1,3])
