class Operand():
    operand = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'eight',
                9: 'Nine'
            }
class OperandString(Operand):
    op = 0
    def __init__(self , op):
        self.op = op
    def toString(self):
        return Operand.operand[self.op]

class OperandNumber(Operand):
    op = 0
    def __init__(self , op):
        self.op = op
    def toString(self):
        return self.op
