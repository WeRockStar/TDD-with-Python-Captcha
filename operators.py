class Operator():
    operator = { 1: '+' , 2 : '-' , 3 : '*' }
    operator_index = 0
    def __init__(self , operator_index):
        self.operator_index = operator_index

    def toString(self):
        return self.operator[self.operator_index]
