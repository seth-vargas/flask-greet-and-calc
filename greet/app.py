from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def get_welcome():
    return "welcome"

@app.route('/welcome/home')
def get_welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def ge_welcome_back():
    return "welcome back"