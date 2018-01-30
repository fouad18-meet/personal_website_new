from flask import Flask, render_template
from flask_bootstrap import Bootstrap 

app = Flask(__name__)
bootstrap = Bootstrap(app)

'''@app.route('/')
def hello_world():
    return '<h1>Hello, Fouad!</h1>'    '''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World'
'''
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
'''