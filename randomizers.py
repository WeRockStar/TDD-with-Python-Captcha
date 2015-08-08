from random import randint
class Randomizer():
    def getPattern(self):
        return randint(1,2)
    def getOperand(self):
        return randint(1,9)
    def getOperator(self):
        return randint(1,3)
