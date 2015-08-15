from radomizer import Randomizer
class CaptchaController():
    def getJson(self , number):
        rand = Randomizer()
        self.json = '{\'left\':%s , \'operand\':1 , \'right\' : 1}'%rand.getOperand()
        return self.json
