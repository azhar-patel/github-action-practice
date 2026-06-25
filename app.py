# adding this file to check linter auto run/action
from flask import Flask, render_template
app = Flask(__name__)
adding this to fail the code


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
