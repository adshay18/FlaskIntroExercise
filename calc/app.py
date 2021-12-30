# Put your app in here.
from flask import Flask, request
from operations import *
app = Flask(__name__)

@app.route('/add')
def add_numbers():
    a = int(request.args['a'])
    b = int(request.args['b'])
    sum = add(a, b)
    return f'{sum}'

@app.route('/sub')
def sub_numbers():
    a = int(request.args['a'])
    b = int(request.args['b'])
    difference = sub(a, b)
    return f'{difference}'

@app.route('/mult')
def mult_numbers():
    a = int(request.args['a'])
    b = int(request.args['b'])
    product = mult(a, b)
    return f'{product}'

@app.route('/div')
def div_numbers():
    a = int(request.args['a'])
    b = int(request.args['b'])
    quotient = div(a, b)
    return f'{quotient}'