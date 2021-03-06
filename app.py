from flask import Flask
from flask.views import MethodView
from fizzbuzz import FizzBuzz
from randomizers import Randomizer

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask"

@app.route('/fizzbuzz/<int:number>')
def fizzbuzz(number):
    fizzbuzz = FizzBuzz()
    return fizzbuzz.count(number)

@app.route('/captcha')
def pattern():
    rand = Randomizer()
    return str(rand.getPattern())

if __name__ == '__main__':
    app.debug = True
    app.run()
