from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    '''Welcomes user to site'''
    return 'welcome'

@app.route('/welcome/home')
def home():
    '''Welcomes user home'''
    return 'welcome home'

@app.route('/welcome/back')
def return_back():
    '''Welcomes user back'''
    return 'welcome back'