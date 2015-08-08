class FizzBuzz():
    def count(self , number):
        if self.isModuloBy3(number) and self.isModuloBy5(number):
            return "FizzBuzz"
        elif self.isModuloBy3(number):
            return 'Fizz'
        elif self.isModuloBy5(number):
            return 'Buzz'
        return str(number)

    def isModuloBy3(self , number):
        return number % 3 == 0

    def isModuloBy5(self , number):
        return number % 5 == 0
