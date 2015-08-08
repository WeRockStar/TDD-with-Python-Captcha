
class Captcha():
    pattern = 0
    def __init__(self , pattern ,left , operator , right):
        self.pattern = pattern
        self.left = left
        self.operator = operator
        self.right = right

    def leftOperator(self):
        return str(self.left)


class SecordPatternOperland():
    left = 0
    right = 0
    patternDigit = {'1' : 'One' , '2' : 'Two'}
    def __init__(self , pattern ,left , operator , right):
        self.pattern = pattern
        self.left = left
        self.operator = operator
        self.right = right

    def leftOperator(self):
        return self.patternDigit[str(self.left)]

    def rightOperator(self):
        return self.patternDigit[str(self.right)]
