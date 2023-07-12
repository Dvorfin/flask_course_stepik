from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact/')
def contact():
    return 'contact information'


@app.route('/calculate/7/9/')
def calculate():
    return str(7 ** 9)


# @app.route('/<int:num>')
# def index(num):
#     return str(num + 1)

@app.route('/<int:num1><string:operator><int:num2>/')
def calc(num1, operator, num2):
    d = {'+': lambda x, y: x+y, '-': lambda x, y: x-y,
         '*': lambda x, y: x*y, ':': lambda x, y: x/y,
         '**': lambda x, y: x**y}
    return str(d[operator](num1, num2))


if __name__ == '__main__':
    app.run(debug=True)
