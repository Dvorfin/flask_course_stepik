from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from config import Config
from project.forms import MessageForm


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['get', 'post'])
def index():
    server_message = ''
    client_message = ''
    if request.method == 'POST':
        client_message = request.form.get('message')

    if client_message == 'hi':
        server_message = 'Hello'
    elif client_message != '':
        server_message = 'How are u?'

    return render_template('index.html', message=server_message)


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


@app.route('/message/', methods=['get', 'post'])
def message():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
        print('\nData received. Now redirecting...')
        return redirect(url_for('message'))

    return render_template('message.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
