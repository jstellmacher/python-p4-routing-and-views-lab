#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:num>')
def count(num):
    count = f''
    for i in range(num):
        count += f'{i}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    return "Operation not recognized please use +, -, *, div, or %."
















# add in the terminal!
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555